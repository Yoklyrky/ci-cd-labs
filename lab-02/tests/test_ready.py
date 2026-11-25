import pytest
import requests
from app import app

def test_ready():
    client = app.test_client()
    response = client.get("/ready")
    assert response.status_code == 200
    assert response.get_json()["ready"] == True
