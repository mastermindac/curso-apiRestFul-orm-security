from fastapi.testclient import TestClient
from api import app,engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
import pytest

# Generamos el Test Cliente
client = TestClient(app)

@pytest.fixture
def db_init():
    try:
        with (engine.connect() as conn):
            #Ahora mismo no hay relaciones pero cuando haya se deberá tener en cuenta para realizar el TRUNCATE
            conn.execute(text("SET FOREIGN_KEY_CHECKS = 0;"))
            conn.execute(text("TRUNCATE TABLE podcasts"))
            conn.execute(text("SET FOREIGN_KEY_CHECKS = 1;"))
            with open("C:/Mastermind/ORM_Security/Masterpodcast/apirestful/api/tests/podcasts.sql") as file:
                for line in file:
                    query = text(line)
                    conn.execute(query)
            conn.commit()
    except SQLAlchemyError as excinfo:
        pytest.fail(f"Se ha producido un error en la conexion o en la consulta: {excinfo}")

# Test del endpoint GET /categories
def test_read_podcasts():
    response = client.get("/podcasts/")
    print(len(response.json()))
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_read_second_podcast(db_init):
    response = client.get("/podcasts/2")
    assert response.status_code == 200
    assert response.json() == {
        "title": "deliver vertical relationships",
        "description": "Praesent lectus. Vestibulum quam sapien, varius ut, blandit non, interdum in, ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio.",
        "url": "http://cyberchimps.com/suspendisse/accumsan/tortor/quis/turpis/sed/ante.xml",
        "id": 2
    }
