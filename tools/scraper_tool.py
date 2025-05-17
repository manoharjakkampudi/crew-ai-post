import warnings
warnings.filterwarnings("ignore")

from crewai.tools import BaseTool
import requests
from bs4 import BeautifulSoup

class ScraperTool(BaseTool):
    name: str = "ScraperTool"
    description: str = "Scrapes a webpage and returns summarized content from it."

    def _run(self, url: str):
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.content, "html.parser")
            paragraphs = soup.find_all("p")
            return "\n".join(p.get_text() for p in paragraphs[:5])
        except Exception as e:
            return f"Error scraping {url}: {str(e)}"
