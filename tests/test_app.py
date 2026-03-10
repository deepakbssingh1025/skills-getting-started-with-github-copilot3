import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_signup_for_activity():
    # Arrange
    activity_name = "Chess Club"
    email = "student1@mergington.edu"
    # Ensure activity exists (depends on app's in-memory state)
    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    # Assert
    assert response.status_code == 200
    assert f"Signed up {email} for {activity_name}" in response.json().get("message", "")
