  <img src="![image](https://github.com/Asman2010/Hikmah-Wealth-Agents/assets/142419243/aea9bd19-4fe8-4bd0-8c18-7fbdf8d282e6)
" width="100" />
</p>
<p align="center">
    <h1 align="center">HIKMAH-WEALTH-AGENTS</h1>
</p>
<p align="center">
    <em><code>Your Intelligent Stock Research Assistant</code></em>

## 🔗 Quick Links

> - [📍 Overview](#-overview)
> - [📦 Features](#-features)
> - [📂 Repository Structure](#-repository-structure)
> - [🧩 Modules](#-modules)
> - [🚀 Getting Started](#-getting-started)
>   - [⚙️ Installation](#️-installation)
>   - [🤖 Running Hikmah-Wealth-Agents](#-running-Hikmah-Wealth-Agents)
> - [📄 License](#-license)
> - [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

Hikmah-Wealth-Agents is an advanced AI-driven platform designed for stock research, focusing on both fundamental and technical analysis of stocks in India. Leveraging powerful AI technologies such as Land Chain and Crew AI, and using the Gemini API along with large language models (LLMs), this tool provides comprehensive insights and analysis to support investors in making informed decisions.

---

## 📦 Features

- **Fundamental Analysis**: In-depth analysis of a company's financial statements, including balance sheets, income statements, and cash flow statements.
- **Technical Analysis**: Evaluation of stock price movements, patterns, and technical indicators to forecast future price trends.
- **Automated News Fetching**: Real-time news aggregation and sentiment analysis to keep you updated on the latest market trends.
- **Comprehensive Reports**: Generation of detailed investment reports including economic analysis, company news analysis, and investment recommendations.
- **User-Friendly Interface**: An intuitive interface built with Streamlit for seamless user experience.

---

## 📂 Repository Structure

```sh
└── Hikmah-Wealth-Agents/
    ├── README.md
    ├── requirements.txt
    ├── scripts.txt
    └── src
        └── app
            ├── .streamlit
            │   └── config.toml
            ├── app.py
            └── backend
                ├── __init__.py
                ├── config
                │   ├── agents.yaml
                │   └── tasks.yaml
                ├── crew.py
                ├── main.py
                ├── reports
                │   ├── Company News Analysis.md
                │   ├── Economic Analysis.md
                │   ├── Final Investment Report.md
                │   ├── Fundamental Analysis.md
                │   └── Investment Analysis.md
                └── tools
                    ├── __init__.py
                    ├── fetch_news.py
                    └── news_sentiment.py
```

---

## 🧩 Modules

<details closed><summary>.</summary>

| File                                                                                                   | Summary                                                       |
| ---                                                                                                    | ---                                                           |
| [scripts.txt](https://github.com/Asman2010/Hikmah-Wealth-Agents.git/blob/master/scripts.txt)           | Contains script references for various automation tasks.      |
| [requirements.txt](https://github.com/Asman2010/Hikmah-Wealth-Agents.git/blob/master/requirements.txt) | Lists the Python dependencies required for the project.       |

</details>

<details closed><summary>src.app</summary>

| File                                                                                       | Summary                                      |
| ---                                                                                        | ---                                          |
| [app.py](https://github.com/Asman2010/Hikmah-Wealth-Agents.git/blob/master/src/app/app.py) | Main application file for the Streamlit app. |

</details>

<details closed><summary>src.app.backend</summary>

| File                                                                                                 | Summary                                                      |
| ---                                                                                                  | ---                                                          |
| [main.py](https://github.com/Asman2010/Hikmah-Wealth-Agents.git/blob/master/src/app/backend/main.py) | Entry point for the backend operations.                      |
| [crew.py](https://github.com/Asman2010/Hikmah-Wealth-Agents.git/blob/master/src/app/backend/crew.py) | Manages the Crew AI functionalities and integrations.        |

</details>

<details closed><summary>src.app.backend.config</summary>

| File                                                                                                                | Summary                                          |
| ---                                                                                                                 | ---                                              |
| [tasks.yaml](https://github.com/Asman2010/Hikmah-Wealth-Agents.git/blob/master/src/app/backend/config/tasks.yaml)   | Configuration for various analysis tasks.        |
| [agents.yaml](https://github.com/Asman2010/Hikmah-Wealth-Agents.git/blob/master/src/app/backend/config/agents.yaml) | Configuration for AI agents and their behaviors. |

</details>

<details closed><summary>src.app..streamlit</summary>

| File                                                                                                            | Summary                                |
| ---                                                                                                             | ---                                    |
| [config.toml](https://github.com/Asman2010/Hikmah-Wealth-Agents.git

/blob/master/src/app/.streamlit/config.toml) | Configuration file for Streamlit setup.|

</details>

---

## 🚀 Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version 3.8+`

### ⚙️ Installation

1. Clone the Hikmah-Wealth-Agents repository:

```sh
git clone https://github.com/Asman2010/Hikmah-Wealth-Agents.git
```

2. Change to the project directory:

```sh
cd Hikmah-Wealth-Agents
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

### 🤖 Running Hikmah-Wealth-Agents

Navigate to src/app folder:

```
cd src/app
```

Use the following command to run Hikmah-Wealth-Agents:

```sh
streamlit run app.py
```

### 🛜 Setup SearXNG

- [Install docker](https://docs.docker.com/install/ "https://docs.docker.com/install/")
- Get searxng-docker
    
    ```sh
    cd /usr/local
    git clone https://github.com/searxng/searxng-docker.git
    cd searxng-docker
    ```
    
- Edit the [.env](https://github.com/searxng/searxng-docker/blob/master/.env "https://github.com/searxng/searxng-docker/blob/master/.env") file to set the hostname and an email
- Generate the secret key `sed -i "s|ultrasecretkey|$(openssl rand -hex 32)|g" searxng/settings.yml`
- When you install SearxNG, the only active output format by default is the HTML format. You need to activate the `json` format to use the API. This can be done by adding the following line to the `settings.yml` file:

```
search:   
	formats:      
		- html       
		- json
```
- Check everything is working: `docker compose up`
- Run SearXNG in the background: `docker compose up -d`

---

## 📄 License

This project is protected under the [MIT License](https://choosealicense.com/licenses/mit/). For more details, refer to the [LICENSE](https://github.com/Asman2010/Hikmah-Wealth-Agents/blob/main/LICENSE) file.

---

## 👏 Acknowledgments

- Developed for the AI Agents Contest hosted by Nvidia and LangChain.
- Thanks to the contributors and the open-source community for their invaluable support and tools.
- Special thanks to the developers of the libraries and frameworks used in this project.
