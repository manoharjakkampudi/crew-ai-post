# crew_runner.py

import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_community.callbacks.manager import get_openai_callback

from crewai import Crew
from agents.agent_factory import load_agents
from tasks.task_factory import load_tasks

# Load environment variables
load_dotenv()

def run_crew(topic: str):
    llm = ChatOpenAI(model="gpt-4", temperature=0.3)

    # Load agents and tasks
    agents = load_agents(topic=topic, llm=llm)
    tasks = load_tasks(agents=agents)

    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        verbose=True
    )

    # Token usage + cost tracking
    with get_openai_callback() as cb:
        result = crew.kickoff()
        print("\n✅ Final Output:\n", result)

        print(f"\n📊 Token Usage:")
        print(f"Prompt Tokens: {cb.prompt_tokens}")
        print(f"Completion Tokens: {cb.completion_tokens}")
        print(f"Total Tokens: {cb.total_tokens}")
        print(f"Estimated Cost: ${cb.total_cost:.4f}")

        # Log usage
        log_entry = {
            "topic": topic,
            "prompt_tokens": cb.prompt_tokens,
            "completion_tokens": cb.completion_tokens,
            "total_tokens": cb.total_tokens,
            "total_cost": cb.total_cost
        }

        os.makedirs("logs", exist_ok=True)
        with open("logs/token_usage.json", "a", encoding="utf-8") as f:
            import json
            f.write(json.dumps(log_entry) + "\n")

if __name__ == "__main__":
    run_crew(topic="AI in Education")
