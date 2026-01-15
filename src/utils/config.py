import os
from pathlib import Path
from dotenv import load_dotenv

# This finds the absolute path to your .env file in the root
env_path = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    DATA_DIR = os.path.join(os.getcwd(), "data")
    DEFAULT_MODEL = "gemini-1.5-flash"

    @classmethod
    def check_config(cls):
        if not cls.GEMINI_API_KEY:
            # Debug print to help you see where it's looking
            print(f"DEBUG: Looking for .env at: {env_path}")
            raise ValueError("CRITICAL ERROR: GEMINI_API_KEY not found in .env")