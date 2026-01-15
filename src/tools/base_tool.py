# src/tools/base_tool.py
from abc import ABC, abstractmethod

class BaseTool(ABC):
    @abstractmethod
    def run(self, *args, **kwargs):
        pass