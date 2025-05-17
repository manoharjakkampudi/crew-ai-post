import warnings
warnings.filterwarnings("ignore")

import yaml
import os
from crewai import Agent
from tools.serper_tool import SerperTool
from tools.scraper_tool import ScraperTool
from tools.post_formatter import PostFormatterTool
from tools.publisher_tool import PublisherTool

TOOLS_MAP = {
    "SerperTool": SerperTool(),
    "ScraperTool": ScraperTool(),
    "PostFormatterTool": PostFormatterTool(),
    "PublisherTool": PublisherTool(),
}

def load_agents(topic: str, path='config/agents.yaml', llm=None):
    with open(path, 'r') as file:
        config = yaml.safe_load(file)

    agents = {}
    for agent_id, attrs in config.items():
        role = attrs['role'].replace('{topic}', topic)
        goal = attrs['goal'].replace('{topic}', topic)
        backstory = attrs['backstory'].replace('{topic}', topic)
        tools = [TOOLS_MAP[t] for t in attrs.get('tools', []) if t in TOOLS_MAP]

        agent = Agent(
            role=role,
            goal=goal,
            backstory=backstory,
            tools=tools,
            verbose=True,
            llm=llm
        )
        agents[agent_id] = agent

    return agents