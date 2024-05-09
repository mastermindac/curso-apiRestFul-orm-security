from sqlalchemy import select
from api import CategoryModel
from api import CategoryCreateSchema

# Controller de categorias
def get_categories(db):
    #Crearia la consulta SELECT * from categories
    stmt = select(CategoryModel)
    #Lista de categorias
    result = db.scalars(stmt)
    categories=result.all()
    return categories

def write_category(db, category: CategoryCreateSchema):
    #Crearemos el modelo ORM a partir del Schema
    categoryModel = CategoryModel(name=category.name)
    #Insertamos en la DB
    db.add(categoryModel)
    #Commit
    db.commit()
    db.refresh(categoryModel)
    return categoryModel

def update_category(db, cat_id:int,category: CategoryCreateSchema):
    #Select del modelo ORM
    categoryModel = db.execute(select(CategoryModel).filter_by(id=cat_id)).scalar_one()
    #Modificamos el name
    categoryModel.name=category.name
    #Commit
    db.commit()
    db.refresh(categoryModel)
    return categoryModel