# src/agents/reflection.py
import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class ReflectionAgent:
    def __init__(self):
        # Securely retrieves key from environment variable or Streamlit secrets
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key and hasattr(st, "secrets") and "GROQ_API_KEY" in st.secrets:
            api_key = st.secrets["GROQ_API_KEY"]
            
        if api_key:
            self.client = Groq(api_key=api_key)
        else:
            self.client = None

    def audit_and_draft(self, transaction_data):
        # Step 1: Initial Reasoning
        initial_prompt = f"Audit this payment: {transaction_data}. Draft a professional receipt."
        # ... agent logic here ...
        
        # Step 2: Self-Reflection Loop
        reflection_prompt = "Review your previous draft for errors in student ID or amount."
        # ... logic to refine and return final content ...
        
        return "Final Draft Content", "Reflection: No errors found. Accuracy 100%."
