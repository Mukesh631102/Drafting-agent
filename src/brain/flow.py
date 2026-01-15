from langgraph.graph import StateGraph, END
from src.brain.state import AgentState
from src.agents.researcher import Researcher
from src.agents.writer import Writer
from src.agents.editor import Editor

def create_drafting_graph():
    workflow = StateGraph(AgentState)

    # Initialize Nodes
    researcher = Researcher()
    writer = Writer()
    editor = Editor()

    # Add Nodes
    workflow.add_node("researcher", researcher.research)
    workflow.add_node("writer", writer.draft)
    workflow.add_node("editor", editor.evaluate)

    # Define the Path
    workflow.set_entry_point("researcher")
    workflow.add_edge("researcher", "writer")
    workflow.add_edge("writer", "editor")

    # Conditional Logic: Does the Editor approve?
    def should_continue(state: AgentState):
        if "PASSED" in state["editor_feedback"]:
            return END
        # If the editor has gone through 3 loops, stop anyway to save money
        if state.get("revision_number", 0) >= 3:
            return END
        return "writer"

    workflow.add_conditional_edges("editor", should_continue)

    return workflow.compile()