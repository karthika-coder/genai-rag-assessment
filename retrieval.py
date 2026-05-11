from embeddings import EmbeddingGenerator
from storage import VectorStore

class RetrievalEngine:
    def __init__(self, dataset):
        self.embedder = EmbeddingGenerator()
        self.store = None
        self.dataset = dataset

    def build_index(self):
        embeddings = self.embedder.generate(self.dataset)
        self.store = VectorStore(embeddings.shape[1])
        self.store.add(embeddings, self.dataset)

    def strategy_a(self, query):
        q_embed = self.embedder.generate([query])[0]
        return self.store.search(q_embed)

    def strategy_b(self, query):
        # Mock query expansion
        expanded_query = query + " system scaling performance high demand"
        q_embed = self.embedder.generate([expanded_query])[0]
        return self.store.search(q_embed)
