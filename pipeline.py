from retrieval import RetrievalEngine

# Example dataset (replace with 5-10 technical paragraphs)
dataset = [
    "System scales horizontally using load balancers.",
    "Peak traffic managed with auto-scaling groups.",
    "Caching reduces DB stress during spikes.",
    "Distributed queues handle high demand efficiently.",
    "Load balancers route traffic evenly across servers."
]

def main():
    engine = RetrievalEngine(dataset)
    engine.build_index()

    queries = [
        "How does the system handle peak load?",
        "What happens during traffic spikes?",
        "Explain scaling under high demand."
    ]

    results = {}
    for q in queries:
        results[q] = {
            "Strategy A": engine.strategy_a(q),
            "Strategy B": engine.strategy_b(q)
        }

    # Save benchmark report
    with open("retrieval_benchmark.md", "w") as f:
        for q, res in results.items():
            f.write(f"### Query: {q}\n\n")
            f.write("**Strategy A (Raw Vector Search):**\n")
            for r in res["Strategy A"]:
                f.write(f"- {r}\n")
            f.write("\n**Strategy B (Query Expansion):**\n")
            for r in res["Strategy B"]:
                f.write(f"- {r}\n")
            f.write("\n\n")

if __name__ == "__main__":
    main()
