import os
from groq import Groq

class ReflectionAgent:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)
        self.model = "llama3-70b-8192" # High-reasoning model for reflection

    def reflect_and_refine(self, student_data, initial_draft):
        """
        Executes a two-stage reflection loop:
        1. Critique the initial draft for accuracy and tone.
        2. Refine the draft based on that critique.
        """
        
        # --- STAGE 1: THE CRITIQUE ---
        critique_prompt = f"""
        You are an expert Financial Auditor and Tone Reviewer. 
        Review the following AI-generated draft against the student's actual financial data.
        
        STUDENT DATA: {student_data}
        AI DRAFT: {initial_draft}
        
        CHECKLIST:
        1. MATH: Does the balance mentioned match (Tuition - Paid)?
        2. TONE: Is it professional yet empathetic for an educational setting?
        3. ACCURACY: Is the student name and ID correct?
        
        Provide only a list of specific improvements needed. If perfect, say 'APPROVED'.
        """
        
        critique_response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "system", "content": "You are a senior financial auditor."},
                      {"role": "user", "content": critique_prompt}]
        )
        critique = critique_response.choices[0].message.content

        if "APPROVED" in critique.upper():
            return initial_draft, "No changes needed. Logic verified."

        # --- STAGE 2: THE REFINEMENT ---
        refinement_prompt = f"""
        The previous draft had these issues: {critique}
        Rewrite the final draft perfectly, incorporating all fixes.
        
        ORIGINAL DATA: {student_data}
        """
        
        final_response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "system", "content": "You are an expert drafting assistant."},
                      {"role": "user", "content": refinement_prompt}]
        )
        
        final_draft = final_response.choices[0].message.content
        return final_draft, critique