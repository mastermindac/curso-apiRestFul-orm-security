from sqlmodel import select
from api import CategoryModel

# Controller de categorias
def get_categories(db):
    #Crearia la consulta SELECT * from categories
    stmt = select(CategoryModel)
    #Lista de categorias
    results = db.exec(stmt)
    categories = results.all()
    return categories
