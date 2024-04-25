from api import engine
import pytest
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

#Comprobacion de la conexion contra la BBDD
#https://docs.sqlalchemy.org/en/20/core/exceptions.html
def test_connection_database_ok():
    try:
        with (engine.connect() as connection):
            result = connection.execute(text("select name from categories"))
            rows = result.all()
            assert len(rows)>0
    except SQLAlchemyError as excinfo:
            pytest.fail(f"Se ha producido un error en la conexion o en la consulta: {excinfo}")