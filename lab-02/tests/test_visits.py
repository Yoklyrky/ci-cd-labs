import pytest
import requests
import os
from app import app

def test_visits():
    client = app.test_client()
    response_1 = client.get("/visits")
    response_2 = client.get("/visits")

    assert response_1.status_code == 200 and response_2.status_code == 200
    assert response_2.get_json()['visits'] == response_1.get_json()['visits'] + 1
