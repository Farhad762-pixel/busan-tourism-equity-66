"""Additional experimental search route; all original endpoints stay unchanged."""
from functools import lru_cache
from pathlib import Path
from fastapi import APIRouter, HTTPException, Query
from src.hybrid_search import HybridRetriever, load_catalog

router = APIRouter()
CATALOG = Path(__file__).resolve().parents[2] / "data/processed/busan_attractions.csv"


@lru_cache(maxsize=1)
def _retriever():
    return HybridRetriever(load_catalog(CATALOG))


@router.get("/api/recommend/hybrid")
def hybrid_search(query: str = Query(..., min_length=1),
                  limit: int = Query(10, ge=1, le=30)):
    try:
        return _retriever().search(query, limit)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
