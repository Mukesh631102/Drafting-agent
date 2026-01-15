import os
from src.utils.config import Config

class FileTool:
    def __init__(self):
        self.target_dir = Config.DATA_DIR
        os.makedirs(self.target_dir, exist_ok=True)

    def save_document(self, filename: str, content: str):
        # Ensure filename is safe and ends in .md for markdown formatting
        if not filename.endswith(".md"):
            filename += ".md"
            
        file_path = os.path.join(self.target_dir, filename)
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return f"SUCCESS: Draft saved to {file_path}"
        except Exception as e:
            return f"TOOL ERROR: {str(e)}"