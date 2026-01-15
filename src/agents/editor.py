from langchain_anthropic import ChatAnthropic
from src.brain.state import AgentState

class Editor:
    def __init__(self):
        self.llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")

    def evaluate(self, state: AgentState):
        print("--- EDITING & EVALUATING ---")
        draft = state['draft']
        
        prompt = f"""
        Review this draft for clarity, tone, and completeness:
        {draft}
        
        If the draft is excellent, respond with 'PASSED'.
        If it needs work, provide specific bullet points for improvement.
        """
        
        response = self.llm.invoke(prompt)
        # We store the feedback to guide the next writing iteration
        return {"editor_feedback": response.content}