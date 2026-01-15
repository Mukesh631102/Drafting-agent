import os
import time
from datetime import datetime
from src.brain.llm_client import Brain

class DraftingAgent:
    def __init__(self):
        self.brain = Brain()
        self.output_dir = "outputs"
        
        # Ensure output directory exists
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def run(self, task_type, data_input):
        """
        Executes a 2-step drafting workflow:
        1. Reasoning/Planning: Model analyzes data for financial accuracy.
        2. Drafting: Model generates the final formal document.
        """
        
        # Step 1: Reasoning & Data Analysis
        # We tell GPT OSS 120B to focus on the 'hidden' logic first
        analysis_prompt = f"""
        Perform a deep financial analysis and logical outline for this {task_type}.
        CONTEXT DATA: {data_input}
        
        Analyze for:
        - Mathematical consistency
        - Potential budget discrepancies
        - Strategic alignment for an educational institution
        
        Provide only the structured outline and key findings.
        """
        
        print(f"[*] Phase 1: Reasoning for {task_type}...")
        reasoning_plan = self.brain.generate_draft(analysis_prompt, persona_type="Financial Auditor")
        
        # Small delay to respect Groq burst limits (though 120B is fast)
        time.sleep(1)

        # Step 2: Formal Drafting
        draft_prompt = f"""
        Using the following analysis, write the FINAL formal {task_type} document.
        ANALYSIS/OUTLINE: {reasoning_plan}
        ORIGINAL DATA: {data_input}
        
        STYLE REQUIREMENTS:
        - Professional, executive tone.
        - No 'AI-style' conversational filler.
        - Use standard professional document headers.
        """
        
        print(f"[*] Phase 2: Generating Final {task_type} Draft...")
        final_draft = self.brain.generate_draft(draft_prompt, persona_type="Chief Financial Officer")

        # Save to file
        filename = f"{task_type.lower().replace(' ', '_')}_{datetime.now().strftime('%H%M%S')}.md"
        file_path = os.path.join(self.output_dir, filename)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(final_draft)
            
        return file_path