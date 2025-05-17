import warnings
warnings.filterwarnings("ignore")

from crewai.tools import BaseTool

class PostFormatterTool(BaseTool):
    name: str = "PostFormatterTool"
    description: str = "Formats social media posts with hashtags and emojis."

    def _run(self, content: str):
        lines = content.split('\n')
        formatted = []
        for line in lines:
            if line.strip():
                formatted.append(f"✨ {line.strip()} #AI #Tech #Automation")
        return "\n".join(formatted)
