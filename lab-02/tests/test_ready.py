import pytest
import requests

def test_ready():
    response = requests.get("http://localhost:8080/ready")
    assert response.status_code == 200
    assert response.json()["ready"] == True
