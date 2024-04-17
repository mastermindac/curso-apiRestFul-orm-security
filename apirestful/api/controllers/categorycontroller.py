from api import engine
from sqlalchemy import text


# Controller de categorias
def get_categories(db):
    # --> SUSTUIR POR EL ORM
    categories=[]
    # comprobamos la correcta conexion
    with engine.connect() as connection:
        result = connection.execute(text("select name from categories"))
        for row in result:
            categories.append({"nombre:": row.name})
    # --> SUSTUIR POR EL ORM
    return categories
