from langchain_anthropic import ChatAnthropic
from src.brain.state import AgentState

class Writer:
    def __init__(self):
        self.llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")

    def draft(self, state: AgentState):
        print("--- WRITING INITIAL DRAFT ---")
        notes = state['research_notes']
        feedback = state.get('editor_feedback', "None")
        
        prompt = f"""
        You are an expert technical writer. 
        Research Notes: {notes}
        Editor Feedback (if any): {feedback}
        
        Task: Create a professional, detailed draft based on the notes. 
        If there is feedback, revise the draft to address all points.
        Format: Use Markdown.
        """
        
        response = self.llm.invoke(prompt)
        return {"draft": response.content}