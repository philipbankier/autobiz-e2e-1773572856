"""
Unit tests for the health-check endpoint (main.py).
Run with: pytest test_main.py -v
"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_check_returns_200():
    response = client.get("/health")
    assert response.status_code == 200


def test_health_check_status_ok():
    response = client.get("/health")
    data = response.json()
    assert data["status"] == "ok"


def test_health_check_company_slug():
    response = client.get("/health")
    data = response.json()
    assert data["company"] == "e2e-1773572856"


def test_health_check_has_timestamp():
    response = client.get("/health")
    data = response.json()
    assert "timestamp" in data
    assert data["timestamp"]  # non-empty


def test_status_endpoint_returns_200():
    response = client.get("/status")
    assert response.status_code == 200


def test_status_endpoint_has_departments():
    response = client.get("/status")
    data = response.json()
    assert "departments" in data
    assert len(data["departments"]) == 6


def test_status_endpoint_company_id():
    response = client.get("/status")
    data = response.json()
    assert data["company"]["id"] == "4357971e-7fa3-4e4f-83fb-b25cae71b3ab"


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "health" in data
