import pytest
from app import app

@pytest.fixture
def paired_names():
    return [
        ("monica", "acinom"),
        ("erica", "acire"),
        ("rita", "atir"),
        ("tina", "anit"),
        ("sandra", "ardnas"),
        ("mary", "yram"),
        ("jessica", "acissej")
    ]

@pytest.fixture
def api():
    return app.test_client()

@pytest.fixture
def bee_data():
    return {
        "id": 1,
        "name": "Beeryl",
        "queen": False
    }