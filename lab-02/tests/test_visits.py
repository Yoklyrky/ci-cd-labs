import pytest
import requests
import app as app_module
from app import app
file = "visits.txt"

def test_visits(monkeypatch, tmp_path):
    monkeypatch.setattr(app_module, "COUNTER_FILE", tmp_path / file)
    client = app.test_client()
    response_1 = client.get("/visits")
    response_2 = client.get("/visits")

    assert response_1.status_code == 200 and response_2.status_code == 200
    assert response_2.get_json()['visits'] == response_1.get_json()['visits'] + 1
