import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Brain:
    def __init__(self):
        # Securely get the API key from environment variables
        # Make sure your .env has: GROQ_API_KEY=gsk_...
        api_key = os.getenv("GROQ_API_KEY")
        
        if not api_key:
            raise ValueError("GROQ_API_KEY not found. Please check your .env file.")
            
        self.client = Groq(api_key=api_key)
        self.model_id = os.getenv("GROQ_MODEL_ID", "openai/gpt-oss-120b")

    def generate_draft(self, prompt: str, persona_type: str = "Financial"):
        """
        Generates a draft using Groq's GPT OSS 120B model.
        Fixed argument name 'persona_type' to match the DraftingAgent call.
        """
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system", 
                        "content": f"You are a professional {persona_type}. Use a formal, audit-ready tone."
                    },
                    {"role": "user", "content": prompt}
                ],
                model=self.model_id,
                # High reasoning effort is essential for financial accuracy in 120B models
                extra_body={
                    "reasoning_effort": "high" 
                },
                temperature=0.1, # Low temperature ensures consistency in data handling
            )
            # Return the text content from the response
            return chat_completion.choices[0].message.content
            
        except Exception as e:
            # Re-raise error to be caught by the Streamlit UI
            raise e