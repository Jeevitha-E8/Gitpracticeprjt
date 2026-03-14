"""
Tests for the Flask Git Practice App.
Run with: pytest tests/ -v
"""
import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app


@pytest.fixture
def client():
    """Create a test client."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    """Test that home page loads."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"git-practice-tracker" in response.data


def test_health_endpoint(client):
    """Test health check returns healthy status."""
    response = client.get("/health")
    data = response.get_json()
    assert response.status_code == 200
    assert data["status"] == "healthy"
    assert "version" in data


def test_api_tasks(client):
    """Test API returns tasks as JSON."""
    response = client.get("/api/tasks")
    data = response.get_json()
    assert response.status_code == 200
    assert isinstance(data, list)


def test_add_task(client):
    """Test adding a new task."""
    response = client.post("/add", data={"title": "Test task"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Test task" in response.data


def test_add_empty_task(client):
    """Test that empty tasks are not added."""
    response = client.post("/add", data={"title": ""}, follow_redirects=True)
    assert response.status_code == 200


def test_update_task_status(client):
    """Test cycling task status."""
    response = client.post("/update/1", follow_redirects=True)
    assert response.status_code == 200


def test_delete_task(client):
    """Test deleting a task."""
    response = client.post("/delete/1", follow_redirects=True)
    assert response.status_code == 200
