import warnings
warnings.filterwarnings("ignore")

from crewai.tools import BaseTool
import requests
import os

class SerperTool(BaseTool):
    name: str = "SerperTool"
    description: str = "Uses Serper API to search Google and return top article URLs."

    def _run(self, query: str):
        api_key = os.getenv("SERPER_API_KEY")
        if not api_key:
            return "Missing SERPER_API_KEY in environment."

        headers = {
            "X-API-KEY": api_key,
            "Content-Type": "application/json"
        }

        data = {"q": query, "num": 3}
        response = requests.post("https://google.serper.dev/search", headers=headers, json=data)
        if response.status_code != 200:
            return f"Error: {response.text}"

        results = response.json().get("organic", [])
        return "\n".join([f"{item['title']}: {item['link']}" for item in results])
