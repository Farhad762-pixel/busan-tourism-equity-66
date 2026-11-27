"""Development diagnostic; counts are NOT human-rated accuracy or a hold-out test."""
import csv
import json
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.hybrid_search import HybridRetriever, load_catalog

ROOT = Path(__file__).resolve().parents[2]
FIELDS = ("main_title", "subtitle", "place", "district", "address", "transport_info")


def run():
    rows = load_catalog(ROOT / "data/processed/busan_attractions.csv")
    queries_path = ROOT / "experiments/equity/benchmark/development_queries.csv"
    with queries_path.open(encoding="utf-8", newline="") as f:
        queries = list(csv.DictReader(f))
    docs = [" ".join(str(row.get(key) or "") for key in FIELDS) for row in rows]
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(docs)
    improved = HybridRetriever(rows)
    output = []
    for row in queries:
        query = row["query"]
        old = cosine_similarity(vectorizer.transform([query]), vectors)[0]
        result = improved.search(query, 10)
        output.append({"query_id": row["query_id"], "query": query,
                       "legacy_positive": sum(float(x) > 0 for x in old),
                       "v2_supported": len(result["supported"]),
                       "v2_related_unverified": len(result["related_unverified"]),
                       "required_evidence": ";".join(result["required_evidence"])})
    result_dir = ROOT / "work" / "retrieval_development"
    result_dir.mkdir(parents=True, exist_ok=True)
    with (result_dir / "audit.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(output[0]))
        writer.writeheader()
        writer.writerows(output)
    summary = {"research_status": "DEVELOPMENT ONLY; not external validation",
               "source_attractions": len(rows), "queries": len(output),
               "legacy_zero_matches": sum(x["legacy_positive"] == 0 for x in output),
               "v2_supported_any": sum(x["v2_supported"] > 0 for x in output),
               "v2_related_any": sum(x["v2_related_unverified"] > 0 for x in output),
               "warning": "Source text matching is NOT independently judged relevance."}
    (result_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    run()
