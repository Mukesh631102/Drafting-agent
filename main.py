from src.agents.drafting_agent import DraftingAgent

def main():
    # Initialize our Pro Agent
    agent = DraftingAgent()
    
    # Execute a sample task
    topic = "The Future of Agentic AI 2026"
    instructions = "Include sections on modularity and Gemini-1.5 integration."
    
    print(f"Starting Agentic Workflow...")
    output = agent.run(topic, instructions)
    print(output)

if __name__ == "__main__":
    main()