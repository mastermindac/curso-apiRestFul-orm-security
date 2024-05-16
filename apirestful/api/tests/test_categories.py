from fastapi.testclient import TestClient
from api import app,engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
import pytest

# Generamos el Test Cliente
client = TestClient(app)

@pytest.fixture
def db_init():
    #Borra todos los datos de DB/Table Category
    try:
        with (engine.connect() as conn):
            #Ahora mismo no hay relaciones pero cuando haya se deberá tener en cuenta para realizar el TRUNCATE
            conn.execute(text("SET FOREIGN_KEY_CHECKS = 0;"))
            conn.execute(text("TRUNCATE TABLE categories"))
            conn.execute(text("SET FOREIGN_KEY_CHECKS = 1;"))
            conn.execute(text("INSERT INTO categories (name) VALUES (:name)"),[
                {"name": "music"},{"name": "technology"},{"name": "food"},{"name": "sports"},{"name": "art"}])
            conn.commit()
    except SQLAlchemyError as excinfo:
            pytest.fail(f"Se ha producido un error en la conexion o en la consulta: {excinfo}")


@pytest.fixture
def db_init_cat_test():
    try:
        with (engine.connect() as conn):
            #Ahora mismo no hay relaciones pero cuando haya se deberá tener en cuenta para realizar el TRUNCATE
            conn.execute(text("SET FOREIGN_KEY_CHECKS = 0;"))
            conn.execute(text("TRUNCATE TABLE categories"))
            conn.execute(text("SET FOREIGN_KEY_CHECKS = 1;"))
            conn.execute(text("INSERT INTO categories (name) VALUES (:name)"),[
                {"name": "music"},{"name": "technology"},{"name": "food"},{"name": "sports"},{"name": "art"},{"name": "test"},
            ])
            conn.commit()
    except SQLAlchemyError as excinfo:
            pytest.fail(f"Se ha producido un error en la conexion o en la consulta: {excinfo}")
# Test del endpoint GET /categories
def test_read_categories():
    response = client.get("/categories/")
    print(len(response.json()))
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_read_second_category():
    response = client.get("/categories/2")
    assert response.status_code == 200
    assert response.json() == {
        "name": "technology",
        "id": 2
    }

# Test del endpoint POST /categories
def test_insert_category(db_init):
    response = client.post(
        "/categories/",
        json={"name": "Test Category"}
    )
    last_category = response.json()
    assert response.status_code == 200
    assert response.json() == {
        "name": "Test Category",
        "id": 6
    }

def test_delete_category(db_init_cat_test):
    response = client.delete("/categories/6")
    assert response.status_code == 200
    assert len(response.json()) == 5