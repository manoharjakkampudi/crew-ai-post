import warnings
warnings.filterwarnings("ignore")

from crewai.tools import BaseTool
import datetime
import os

class PublisherTool(BaseTool):
    name: str = "PublisherTool"
    description: str = "Simulates publishing content to social media or blog platforms."

    def _run(self, content: str):
        platform = os.getenv("PUBLISH_PLATFORM", "SimulatedPlatform")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        simulated_response = (
            f"[{timestamp}] ✅ Content successfully published to {platform}:\n\n{content}\n"
        )

        os.makedirs("logs", exist_ok=True)
        with open("logs/published_content.log", "a", encoding="utf-8") as log:
            log.write(simulated_response + "\n" + ("-" * 40) + "\n")

        return simulated_response
