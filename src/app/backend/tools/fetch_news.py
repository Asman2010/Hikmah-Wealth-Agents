from gnews import GNews
from crewai_tools import tool
from langchain_community.utilities import SearxSearchWrapper
import requests

@tool("Search News")
def search_news(query: str):  
    """Search the news on the web for the given query and return the results. Takes Arguement 'query' as a string."""
    google_news = GNews(language='en', country='IN', period='7d', max_results=20)
    news = google_news.get_news(query)
    titles = [article['title'] for article in news]
    
    return titles
    
    
@tool("Search Internet")
def search_web(query: str) -> str:
    """Search the web for the given query and return the results. Takes Arguement 'query' as a string."""
    
    host = "http://127.0.0.1:8080"
    
    def seax():
        
        url = host
        params = {
            "q": query,
            "format": "json"
        }
        
        new = requests.get(url, params=params).json()
        results = new['results']
        print(new)
        print("-" * 100 )
        for result in results:
            title = f"Title: {result['title']}"
            content = f"Content: {result['content']}"
            url = f"URL: {result['url']}"
            date = f"Published Date: {result.get('publishedDate', 'Not available')}"
            search_engine = f"Search Engine: {result['engine']}"
            
            return f"{title}\n{content}\n{url}\n{date}\n{search_engine}"

    s = SearxSearchWrapper(searx_host=host)
    langchain = s.run(query=query)
    
    return [seax(), langchain]

