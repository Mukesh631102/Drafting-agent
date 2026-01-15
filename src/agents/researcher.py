from langchain_google_genai import ChatGoogleGenerativeAI
from src.brain.state import AgentState
from src.tools.web_search import SearchTool

class Researcher:
    def __init__(self):
        # Using Gemini 1.5 Flash - it's the best for the free tier
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
        self.search_tool = SearchTool()

    def research(self, state: AgentState):
        task = state['task']
        print(f"--- RESEARCHING: {task} ---")
        
        # 1. Ask Gemini what to search for
        search_query = self.llm.invoke(f"Based on this task: '{task}', what is the single best search query to find facts?").content
        
        # 2. Use the free DuckDuckGo tool
        results = self.search_tool.run(search_query)
        
        return {
            "research_notes": [results],
            "revision_number": state.get("revision_number", 0) + 1
        }