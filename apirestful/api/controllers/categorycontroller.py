from sqlalchemy import select
from api import CategoryModel
from api import CategoryCreateSchema
from sqlalchemy.exc import NoResultFound, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError


# Controller de categorias
def get_categories(db):
    try:
        # Crearia la consulta SELECT * from categories
        stmt = select(CategoryModel)
        # Lista de categorias
        result = db.scalars(stmt)
        categories = result.all()
    except OperationalError:
        categories = None
    return categories


def get_category(db, cat_id: int):
    try:
        # Select del modelo ORM
        result = db.execute(select(CategoryModel).filter_by(id=cat_id))
        categoryModel = result.scalar_one()
    except NoResultFound:
        categoryModel = None
    return categoryModel


def write_category(db, category: CategoryCreateSchema):
    # Crearemos el modelo ORM a partir del Schema
    categoryModel = CategoryModel(name=category.name)
    # Insertamos en la DB
    db.add(categoryModel)
    # Commit
    db.commit()
    db.refresh(categoryModel)
    return categoryModel


def update_category(db, cat_id: int, category: CategoryCreateSchema):
    try:
        # Select del modelo ORM
        result = db.execute(select(CategoryModel).filter_by(id=cat_id))
        categoryModel = result.scalar_one()
        # Modificamos el name
        categoryModel.name = category.name
        # Commit
        db.commit()
        db.refresh(categoryModel)
    except NoResultFound:
        categoryModel = None
    return categoryModel


def delete_category(db, cat_id: int, ):
    try:
        # Select del modelo ORM
        category = db.get(CategoryModel, cat_id)
        db.delete(category)
        db.commit()
        categories = get_categories(db)
    except UnmappedInstanceError:
        categories = None
    return categories
