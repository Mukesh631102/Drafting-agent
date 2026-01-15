import chromadb
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

class MemoryManager:
    def __init__(self):
        # This model runs locally on your CPU for free
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.vector_store = Chroma(
            persist_directory="./data/chroma_db",
            embedding_function=self.embeddings,
            collection_name="writing_style"
        )

    def learn_style(self, text_list):
        """Add your past writings so the agent can mimic you."""
        self.vector_store.add_texts(text_list)
        print("Agent has updated its memory of your style.")

    def get_context(self, query):
        """Find the most relevant past examples for a new draft."""
        results = self.vector_store.similarity_search(query, k=2)
        return "\n".join([doc.page_content for doc in results])