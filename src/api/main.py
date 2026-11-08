import csv
from collections import Counter
from pathlib import Path
from typing import Literal

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ATTRACTIONS_CSV = (
    Path(__file__).resolve().parents[2] / "data/processed/busan_attractions.csv"
)


class Attraction(BaseModel):
    id: int
    name: str
    district: str
    latitude: float
    longitude: float
    address: str
    place: str


class Recommendation(BaseModel):
    id: int
    name: str
    district: str
    latitude: float
    longitude: float
    address: str
    relevance_score: float


class EquityRecommendation(Recommendation):
    equity_score: float
    final_score: float
    equity_measure: Literal["prototype_attraction_distribution_proxy"] = (
        "prototype_attraction_distribution_proxy"
    )


class RecommendationComparison(BaseModel):
    baseline: list[Recommendation]
    equity_aware: list[EquityRecommendation]
    baseline_unique_districts: int
    equity_aware_unique_districts: int


app = FastAPI(title="Busan Tourism Equity Recommender")


@app.get("/api/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "project": "Busan Tourism Equity Recommender",
    }


@app.get("/api/attractions", response_model=list[Attraction])
def attractions(district: str | None = None) -> list[Attraction]:
    """Return all attractions, optionally filtered by exact district name."""
    with ATTRACTIONS_CSV.open(encoding="utf-8-sig", newline="") as csv_file:
        return [
            Attraction(
                id=row["uc_seq"],
                name=row["main_title"],
                district=row["district"],
                latitude=row["latitude"],
                longitude=row["longitude"],
                address=row["address"],
                place=row["place"],
            )
            for row in csv.DictReader(csv_file)
            if district is None or row["district"] == district
        ]


@app.get("/api/recommend/baseline", response_model=list[Recommendation])
def recommend_baseline(
    query: str = Query(..., min_length=1),
    limit: int = Query(10, ge=1),
) -> list[Recommendation]:
    """Rank attractions by TF-IDF cosine similarity; ties follow CSV order."""
    return _baseline_ranking(query)[:limit]


def _baseline_ranking(query: str) -> list[Recommendation]:
    if not query.strip():
        raise HTTPException(status_code=422, detail="query must contain text")

    with ATTRACTIONS_CSV.open(encoding="utf-8-sig", newline="") as csv_file:
        rows = list(csv.DictReader(csv_file))

    text_fields = (
        "main_title", "subtitle", "place", "district", "address", "transport_info"
    )
    documents = [" ".join(row[field] for field in text_fields) for row in rows]
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(documents)
    scores = cosine_similarity(vectorizer.transform([query]), vectors)[0]
    ranked_indices = sorted(range(len(rows)), key=lambda i: -float(scores[i]))

    return [
        Recommendation(
            id=rows[i]["uc_seq"],
            name=rows[i]["main_title"],
            district=rows[i]["district"],
            latitude=rows[i]["latitude"],
            longitude=rows[i]["longitude"],
            address=rows[i]["address"],
            relevance_score=float(scores[i]),
        )
        for i in ranked_indices
    ]


def _equity_ranking(
    baseline: list[Recommendation], limit: int, equity_weight: float
) -> list[EquityRecommendation]:
    counts = Counter(item.district for item in baseline)
    minimum, maximum = min(counts.values()), max(counts.values())
    candidates = []
    for item in baseline[:50]:
        if item.relevance_score <= 0:
            continue
        # Min-max normalize inverse counts; equal counts provide no bonus.
        equity_score = (
            (maximum - counts[item.district]) / (maximum - minimum)
            if maximum != minimum else 0.0
        )
        candidates.append(
            EquityRecommendation(
                **item.model_dump(),
                equity_score=equity_score,
                final_score=(1 - equity_weight) * item.relevance_score
                + equity_weight * equity_score,
            )
        )
    # Stable sorting preserves baseline order for ties.
    return sorted(candidates, key=lambda item: -item.final_score)[:limit]


@app.get("/api/recommend/equity", response_model=list[EquityRecommendation])
def recommend_equity(
    query: str = Query(..., min_length=1),
    limit: int = Query(10, ge=1),
    equity_weight: float = Query(0.20, ge=0, le=1),
) -> list[EquityRecommendation]:
    """Re-rank at most 50 baseline candidates using
    prototype_attraction_distribution_proxy.

    The proxy is (maximum district count - district count) / (maximum - minimum),
    using all CSV attractions. It measures dataset representation only, not real
    economic inequality. Only candidates with positive relevance are re-ranked.
    Returns fewer than limit results when insufficient positive matches exist,
    and at most 50 results even when limit is larger.
    """
    return _equity_ranking(_baseline_ranking(query), limit, equity_weight)


@app.get("/api/compare", response_model=RecommendationComparison)
def compare_recommendations(
    query: str = Query(..., min_length=1),
    limit: int = Query(10, ge=1),
    equity_weight: float = Query(0.20, ge=0, le=1),
) -> RecommendationComparison:
    """Compare baseline and prototype re-ranking with unique district counts.

    prototype_attraction_distribution_proxy measures dataset representation,
    not real economic inequality. Equity results include only positive-relevance
    matches from the top 50 baseline candidates and may be fewer than limit.
    """
    ranking = _baseline_ranking(query)
    baseline = ranking[:limit]
    equity_aware = _equity_ranking(ranking, limit, equity_weight)
    return RecommendationComparison(
        baseline=baseline,
        equity_aware=equity_aware,
        baseline_unique_districts=len({item.district for item in baseline}),
        equity_aware_unique_districts=len({item.district for item in equity_aware}),
    )
