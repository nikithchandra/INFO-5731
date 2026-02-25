"""Unit tests for the FastAPI application"""

import pytest
from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)


def test_root():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to FastAPI Application"


def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_item():
    """Test creating an item"""
    response = client.post(
        "/api/v1/items",
        json={"name": "Test Item", "description": "A test item"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"


def test_get_items():
    """Test retrieving items"""
    response = client.get("/api/v1/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
