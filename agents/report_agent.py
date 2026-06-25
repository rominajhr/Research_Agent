# agents/report_agent.py

class ReportAgent:

    def run(
        self,
        paper,
        analysis,
        summary,
        critic,
        ideas
    ):
        

        markdown = f"""
# Research Analysis Report

## Paper Information

**Title:** {paper["title"]}

**Authors:** {", ".join(paper["authors"])}

**Published:** {paper["published"]}

---

## Research Field

{analysis["research_field"]}

---

## Problem Statement

{analysis["problem"]}

---

## Proposed Method

{analysis["method"]}

---

## Main Results

{analysis["results"]}

---

## Keywords

{", ".join(analysis["keywords"])}

---

## Executive Summary

{summary}

---

## Technical Limitations
"""

        for item in critic["technical_limitations"]:
            markdown += f"\n- {item}"

        markdown += "\n\n## Experimental Limitations\n"

        for item in critic["experimental_limitations"]:
            markdown += f"\n- {item}"

        markdown += "\n\n## Future Directions\n"

        for item in ideas["future_directions"]:
            markdown += f"\n- {item}"

        markdown += "\n\n## Research Ideas\n"

        for item in ideas["research_ideas"]:
            markdown += f"\n- {item}"

        return {

            "paper": {
                "title": paper["title"],
                "authors": paper["authors"],
                "num_authors": len(paper["authors"]),
                "published": paper["published"]
            },

            "research_field": analysis["research_field"],

            "problem": analysis["problem"],

            "method": analysis["method"],

            "results": analysis["results"],

            "keywords": analysis["keywords"],

            "summary": summary,

            "technical_limitations":
                critic["technical_limitations"],

            "experimental_limitations":
                critic["experimental_limitations"],

            "future_directions":
                ideas["future_directions"],

            "research_ideas":
                ideas["research_ideas"],

            "markdown": markdown
        }