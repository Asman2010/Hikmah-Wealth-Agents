import os
import json
import streamlit as st
from typing import Union, List, Tuple, Dict
from crewai import Agent, Crew, Process, Task
from langchain_core.agents import AgentFinish
from crewai.project import CrewBase, agent, crew, task
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

# load env
from dotenv import load_dotenv
load_dotenv()

# pre-built tools
from crewai_tools import WebsiteSearchTool, SerperDevTool

# custom-tools
from backend.tools.news_sentiment import news_analysis
from backend.tools.fetch_news import search_news, search_web


@CrewBase
class HikmahWealthAgentsCrew():
	"""HikmahWealthAgents crew"""

	def __init__(self, query: str):
        
		self.config = {
			"embedder": {
				"provider": "ollama",
				"config": {
					"model": "nomic-embed-text",
					"base_url": "http://127.0.0.1:11434"
				}
			}
		}
		

		self.mistral_nvidia = ChatOpenAI(
			base_url = "https://integrate.api.nvidia.com/v1",
 	 		api_key = os.getenv("NIM"),
			model= "mistralai/mixtral-8x22b-instruct-v0.1"
		)
  
		self.llama2_nvidia = ChatOpenAI(
			base_url = "https://integrate.api.nvidia.com/v1",
			api_key = os.getenv("NIM"),
			model= "meta/llama3-70b-instruct"
		)
		
		self.get_financials = WebsiteSearchTool(website=f"https://www.screener.in/company/{query}/", config=self.config)
		self.agents_config = r"src\hikmah_wealth_agents\config\agents.yaml"
		self.tasks_config = r"src\hikmah_wealth_agents\config\tasks.yaml"
		self.max_iter = 5
		self.max_rpm = 15
		self.search_web = search_web # if searxng is not working use SerperDevTool
		self.news_analysis = news_analysis
		self.search_g_news = search_news
  
		self.output_directory = '.\Reports'
  
	def step_callback(
        self,
        agent_output: Union[str, List[Tuple[Dict, str]], AgentFinish],
        agent_name,
        *args,
    ):
		with st.chat_message("AI"):
			# Try to parse the output if it is a JSON string
			if isinstance(agent_output, str):
				try:
					agent_output = json.loads(agent_output)
				except json.JSONDecodeError:
					pass

			if isinstance(agent_output, list) and all(
				isinstance(item, tuple) for item in agent_output
			):

				for action, description in agent_output:
					# Print attributes based on assumed structure
					st.write(f"**Agent Name**: {agent_name}")
					st.write(f"**Tool used**: {getattr(action, 'tool', 'Unknown')}")
					st.write(f"**Tool input**: {getattr(action, 'tool_input', 'Unknown')}")
					st.write(f"{getattr(action, 'log', 'Unknown')}")
					with st.expander("Show observation"):
						st.markdown(f"Observation\n\n{description}")
					st.divider()


			# Check if the output is a dictionary as in the second case
			elif isinstance(agent_output, AgentFinish):
				st.write(f"Agent Name: {agent_name}")
				output = agent_output.return_values
				st.write(f"I finished my task:\n{output['output']}")
				st.divider()

			# Handle unexpected formats
			else:
				st.write(type(agent_output))
				st.write(agent_output)
				st.divider

	@agent
	def company_news_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['company_news_analyst'],
			verbose=True,
            tools=[self.news_analysis, self.search_web],
            allow_delegation=True,
            llm=self.mistral_nvidia,
            max_rpm=self.max_rpm,
            max_iter=self.max_iter,
            step_callback=lambda step: self.step_callback(step, "Company News Analyst"),
		)

	@agent
	def investment_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['investment_analyst'],
			verbose=True,
            tools=[self.search_web, self.search_g_news],
            allow_delegation=True,
            llm=self.llama2_nvidia,
            max_iter=self.max_iter,
            max_rpm=self.max_rpm,
            step_callback=lambda step: self.step_callback(step, "Investment Research Analyst"),
		)
  
	@agent
	def finanical_data_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['fundamentals_analyst'],
			verbose=True,
   			tools=[self.search_web, self.get_financials, self.search_g_news],
            allow_delegation=True,
            llm=self.llama2_nvidia,
            max_iter=self.max_iter,
            max_rpm=self.max_rpm,
            step_callback=lambda step: self.step_callback(step, "Financial Data Analyst"),
		)

	@agent
	def economic_forecaster(self) -> Agent:
		return Agent(
			config=self.agents_config['economic_forecaster'],
			verbose=True,
            tools=[self.search_web, self.search_g_news],
            allow_delegation=True,
            llm=self.mistral_nvidia,
            max_iter=self.max_iter,
            max_rpm=self.max_rpm,
            step_callback=lambda step: self.step_callback(step, "Economic Forecaster"),
		)

	@agent
	def report_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['report_generator'],
			verbose=True,
    		allow_delegation=False,
            llm=self.llama2_nvidia,
            max_iter=self.max_iter,
            max_rpm=self.max_rpm,
            step_callback=lambda step: self.step_callback(step, "Report Writer"),
		)

	####################### Tasks #######################

	@task
	def company_news_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['company_news_analysis'],
			agent=self.company_news_analyst(),
			output_file = os.path.join(self.output_directory, 'Comapany News Analysis.md')
		)

	@task
	def investment_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['investment_analysis'],
			agent=self.investment_analyst(),
			output_file = os.path.join(self.output_directory, f'Investment Analysis.md')
		)

	@task
	def fundamental_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['fundamental_analysis'],
			agent=self.finanical_data_analyst(),
   			output_file = os.path.join(self.output_directory, f'Fundamental Analysis.md')
		)
  
	@task
	def economic_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['economic_analysis'],
			agent=self.economic_forecaster(),
			output_file = os.path.join(self.output_directory, f'Economic Analysis.md')
		)
  
	@task
	def report_writing_task(self) -> Task:
		return Task(
			config=self.tasks_config['report_writing'],
			agent=self.report_writer(),
			output_file = os.path.join(self.output_directory, f'Final Investment Report.md')
		)
  

	@crew
	def crew(self) -> Crew:
		"""Creates the HikmahWealthAgents crew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
            memory=False,
			embedder={
				"provider": "ollama",
				"config": {
					"model": "nomic-embed-text",
					"base_url": "http://127.0.0.1:11434"
				}
			}
		)
