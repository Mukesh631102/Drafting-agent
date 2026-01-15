# src/tools/draft_writer.py
import os

class DraftTool:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)

    def save_draft(self, filename: str, content: str):
        path = os.path.join(self.data_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Draft saved successfully to {path}"