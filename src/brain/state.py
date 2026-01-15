from typing import Annotated, TypedDict, List
import operator

class AgentState(TypedDict):
    # This keeps track of the user's original goal
    task: str
    # The current outline of the document
    outline: List[str]
    # Collected research data
    research_notes: List[str]
    # The actual draft (updated by the writer)
    draft: str
    # Revision count to prevent infinite loops
    revision_number: int
    # Comments from the Editor agent
    editor_feedback: str