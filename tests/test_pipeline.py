import sys
import os

# Add project root (one level up from tests/) to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipeline import RetrievalEngine, dataset

def test_retrieval_pipeline():
    engine = RetrievalEngine(dataset)
    engine.build_index()
    query = "How does the system handle peak load?"
    assert len(engine.strategy_a(query)) > 0
    assert len(engine.strategy_b(query)) > 0
