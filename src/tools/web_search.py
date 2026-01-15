from langchain_community.tools import DuckDuckGoSearchRun

class SearchTool:
    def __init__(self):
        self.search = DuckDuckGoSearchRun()

    def run(self, query: str):
        print(f"Searching for: {query}")
        return self.search.run(query)