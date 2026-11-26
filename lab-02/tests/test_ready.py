import pytest
import requests
import os
import app as app_module
from app import app
file = "visits.txt"

def test_ready(monkeypatch, tmp_path):
    monkeypatch.setattr(app_module, "COUNTER_FILE", tmp_path / file )
    client = app.test_client()
    response = client.get("/ready")
    assert response.status_code == 200
    assert response.get_json()["ready"] == True
