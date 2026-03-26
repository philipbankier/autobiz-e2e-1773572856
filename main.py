"""
Health-check endpoint for E2E Test Company 2 (e2e-1773572856).
Returns company status as JSON.
"""

from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(title="E2E Test Company 2 API", version="0.1.0")

COMPANY_INFO = {
    "id": "4357971e-7fa3-4e4f-83fb-b25cae71b3ab",
    "slug": "e2e-1773572856",
    "name": "E2E Test Company 2",
    "stage": "planning",
    "mission": "End-to-end testing of the AutoBiz platform — second validation run.",
}


@app.get("/health")
def health_check():
    """Return current company status for health monitoring."""
    return {
        "status": "ok",
        "company": COMPANY_INFO["slug"],
        "name": COMPANY_INFO["name"],
        "stage": COMPANY_INFO["stage"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/status")
def company_status():
    """Return full company status JSON."""
    return {
        "status": "ok",
        "company": COMPANY_INFO,
        "departments": [
            "ceo",
            "developer",
            "finance",
            "marketing",
            "sales",
            "support",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/")
def root():
    """Root — redirect to /health."""
    return {"message": "AutoBiz E2E Test Company 2 API", "docs": "/docs", "health": "/health"}
