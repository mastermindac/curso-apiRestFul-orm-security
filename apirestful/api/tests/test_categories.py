from fastapi.testclient import TestClient
from api import app
import pytest

# Generamos el Test Cliente
client = TestClient(app)


# Generamos un fixture de datos
@pytest.fixture
def last_category():
    return {}


# Test del endpoint GET /categories
def test_read_categories():
    response = client.get("/categories/")
    print(len(response.json()))
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_insert_category(last_category):
    response = client.post(
        "/categories/",
        json={"name": "Foo Bar"},
    )
    last_category = response.json()
    print(last_category)
    assert response.status_code == 200
    assert last_category['name'] == "Foo Bar"

def test_read_last_category(last_category):
    print(last_category)
    assert last_category['name'] == "Foo Bar"