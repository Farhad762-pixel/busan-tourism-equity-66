"""Run: uvicorn src.api.app_v2:app --reload

Original src/api/main.py is NOT changed. This adds one experimental endpoint.
The original /api/recommend/equity remains an attraction-count proxy.
"""
from src.api.main import app
from src.api.hybrid_router import router

app.include_router(router)
