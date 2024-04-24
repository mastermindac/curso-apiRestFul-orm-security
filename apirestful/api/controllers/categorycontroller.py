from sqlalchemy import select
from api import CategoryModel

# Controller de categorias
def get_categories(db):
    #Crearia la consulta SELECT * from categories
    stmt = select(CategoryModel)
    #Lista de categorias
    result = db.scalars(stmt)
    categories=result.all()
    return categories
