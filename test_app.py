import pytest
from practice_functions import add, subtract, reverse


@pytest.mark.parametrize("x, y, z", [(1, 2, 3)])
def test_add(x, y, z):
    assert add(x, y) == z

@pytest.mark.parametrize("x, y, z", [(1, 2, 3)])
def test_subtract(x, y, z):
    assert subtract(z, y) == x
    assert subtract(z, x) == y

def test_reverse(paired_names):
    for name in paired_names:
        assert reverse(name[0]) == name[1]

def test_index(api):

    res = api.get("/")

    assert "Bumble" in res.text
    assert res.status == "200 OK"
    
def test_bees(api):

    res = api.get("/bees")
    
    assert res.status == "200 OK"
    assert res.json["success"] == True
    assert isinstance(res.json["bees"], list)

def test_bees_new_post(api, bee_data):

    res = api.post("/bees/new", json=bee_data)

    assert res.status == "201 CREATED"
    assert res.json["success"] == True
    assert isinstance(res.json["bee"], dict)

def test_bees_new_post_bad(api):

    bad_bee_data = {
        "name": "Roderick"
    }

    res = api.post("/bees/new", json=bad_bee_data)

    assert res.status == "400 BAD REQUEST"
    assert res.json["success"] == False
    assert isinstance(res.json["error"], str)