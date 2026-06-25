# models/analysis_schema.py

from pydantic import BaseModel


class AnalysisSchema(BaseModel):
    research_field: str
    problem: str
    method: str
    results: str

    keywords: list[str]

    summary: str

    technical_limitations: list[str]
    experimental_limitations: list[str]

    future_directions: list[str]
    research_ideas: list[str]