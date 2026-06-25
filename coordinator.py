from agents.search_agent import SearchAgent
from agents.paper_analysis_agent import PaperAnalysisAgent
from agents.summary_agent import SummaryAgent
from agents.critic_agent import CriticAgent
from agents.idea_agent import IdeaAgent
from agents.report_agent import ReportAgent


class Coordinator:

    def __init__(self):

        self.search_agent = SearchAgent()
        self.analysis_agent = PaperAnalysisAgent()

        self.summary_agent = SummaryAgent()
        self.critic_agent = CriticAgent()
        self.idea_agent = IdeaAgent()

        self.report_agent = ReportAgent()

    def run(self, topic):

        # 1. Find paper
        paper = self.search_agent.run(topic)

        # 2. Analyze paper
        analysis = self.analysis_agent.run(paper)
        analysis = self.analysis_agent.run(paper)


        # 3. Extract outputs
        summary = self.summary_agent.run(analysis)

        critic = self.critic_agent.run(analysis)

        ideas = self.idea_agent.run(analysis)

        # 4. Generate final report
        report = self.report_agent.run(
            paper,
            analysis,
            summary,
            critic,
            ideas
        )

        return report