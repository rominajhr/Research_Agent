from google import genai
from google.genai import types

from config import GEMINI_API_KEY
from models.analysis_schema import AnalysisSchema

from tenacity import retry, stop_after_attempt, wait_exponential


class PaperAnalysisAgent:

    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=2)
    )
    def run(self, paper):

        prompt = f"""
        You are an expert research analyst.

        Analyze this research paper.
        Even if limitations are not explicitly mentioned,
        infer likely experimental limitations from the
        paper's methodology and evaluation scope.

        Generate at least:
        - 3 technical limitations
        - 3 experimental limitations
        - 4 future directions
        - 4 research ideas

        Avoid saying information is missing.
        Infer plausible limitations when necessary.

        
        Title:
        {paper["title"]}

        Abstract:
        {paper["abstract"]}

        Generate:

        - research_field
        - problem
        - method
        - results
        - keywords
        - summary
        - technical_limitations
        - experimental_limitations
        - future_directions
        - research_ideas

        Be specific to THIS paper.
        """

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,

            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=AnalysisSchema
            )
        )

        return response.parsed.model_dump()