import requests
import pytest

BASE_URL = "https://cat-fact.herokuapp.com"

def test_get_facts():
    response = requests.get(f"{BASE_URL}/facts")
    assert response.status_code == 200
    facts = response.json()
    assert len(facts) > 0
    assert "text" in facts[0]

def test_get_fact_by_id():
    response = requests.get(f"{BASE_URL}/facts/58e008800aac31001185ed07")
    assert response.status_code == 200
    fact = response.json()
    assert fact["text"] == "Cats make about 100 different sounds. Dogs make only about 10."
