# 🤖 Crew AI AutoPost

An automated AI system built with **CrewAI**, **LangChain**, and **OpenAI** that scrapes trending content, formats it for social media, and simulates publishing — all driven by intelligent multi-agent collaboration.

---

## 🚀 Features

- 🧠 Multi-agent architecture (CrewAI)
- 🔍 Google search via Serper API
- 🌐 Web scraping using BeautifulSoup
- ✨ Post formatting with hashtags & emojis
- 📤 Publishing simulation with logging
- 💰 Tracks OpenAI token usage and cost

---

## 🗂 Project Structure
```
autopost_ai/
│
├── crew_runner.py # Main entrypoint
├── agents/
│ └── agent_factory.py # Agent definitions from YAML
├── tasks/
│ └── task_factory.py # Task definitions from YAML
├── tools/
│ ├── serper_tool.py # Google Search tool
│ ├── scraper_tool.py # Web scraper
│ ├── post_formatter.py # Formats posts for social media
│ └── publisher_tool.py # Simulates publishing
│
├── config/
│ ├── agents.yaml # Agent roles, goals, backstories
│ └── tasks.yaml # Agent-task assignments
│
├── logs/
│ └── token_usage.json # Token + cost tracking (auto-generated)
│
├── .env # API keys and environment variables
├── requirements.txt # Python dependencies
└── README.md # Project documentation

```


## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/manoharjakkampudi/crew-ai-post.git
cd crew-ai-post
```

### 2. Setup virtual environment
```bash
python -m venv venv
.\venv\Scripts\activate  # On Windows
```


###3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Configure Environment Variables
```bash
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
PUBLISH_PLATFORM=Twitter  # Optional
```

### ▶️ Run the Project
```bash
python crew_runner.py
```

📊 Output Example
✅ Final Output:
✨ AI in Education is transforming learning... #AI #Tech #Automation
✨ Top tools include adaptive learning platforms... #AI #Tech #Automation

📊 Token Usage:
Prompt Tokens: 1234
Completion Tokens: 2109
Total Tokens: 3343
Estimated Cost: $0.0678
