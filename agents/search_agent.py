import arxiv


class SearchAgent:

    def run(self, topic):

        search = arxiv.Search(
            query=topic,
            max_results=1,
            sort_by=arxiv.SortCriterion.Relevance
        )
        client = arxiv.Client()

        results = list(client.results(search))

        if not results:
            return None

        paper = results[0]

        return {
            "title": paper.title,
            "authors": [author.name for author in paper.authors],
            "abstract": paper.summary,
            "published": str(paper.published.date()),
            "pdf_url": paper.pdf_url,
            "entry_id": paper.entry_id
        }