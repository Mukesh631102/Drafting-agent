# src/agents/orchestrator.py
from src.brain.llm_client import Brain
from src.tools.draft_writer import DraftTool

class DraftingAgent:
    def __init__(self):
        self.brain = Brain()
        self.writer = DraftTool()

    def run(self, topic: str):
        print(f"Agent: Starting draft for '{topic}'...")
        
        # 1. Brain generates the content
        draft_content = self.brain.think(f"Write a detailed report about {topic}")
        
        # 2. Tool saves the content
        filename = f"{topic.replace(' ', '_')}.txt"
        result = self.writer.save_draft(filename, draft_content)
        
        return result