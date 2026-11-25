import pytest
import requests

def test_visits():
    response_1 = requests.get("http://localhost:8080/visits")
    response_2 = requests.get("http://localhost:8080/visits")

    assert response_1.status_code == 200 and response_2.status_code == 200
    assert response_2.json()['visits'] == response_1.json()['visits'] + 1
