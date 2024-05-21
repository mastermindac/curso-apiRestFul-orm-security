from sqlalchemy import select
from api import AuthorModel, AuthorCreateSchema, AuthorUpdateSchema
from sqlalchemy.exc import NoResultFound, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError


# Controller de podcasts
def get_authors(db):
    try:
        # Crearia la consulta SELECT * from categories
        stmt = select(AuthorModel)
        # Lista de categorias
        result = db.scalars(stmt)
        authors = result.all()
    except OperationalError:
        authors = None
    return authors


def get_author(db, author_id: int):
    try:
        # Select del modelo ORM
        result = db.execute(select(AuthorModel).filter_by(id=author_id))
        authorModel = result.scalar_one()
    except NoResultFound:
        authorModel = None
    return authorModel


def write_author(db, author: AuthorCreateSchema):
    # Crearemos el modelo ORM a partir del Schema
    authorModel = AuthorModel(name=author.name, nationality=author.nationality)
    # Insertamos en la DB
    db.add(authorModel)
    # Commit
    db.commit()
    db.refresh(authorModel)
    return authorModel


def update_author(db, author_id: int, author: AuthorUpdateSchema):
    try:
        # Select del modelo ORM
        result = db.execute(select(AuthorModel).filter_by(id=author_id))
        authorModel = result.scalar_one()
        # Modificamos el podcast
        # Update model class variable from requested fields
        for key, value in author:
            if value is not None: setattr(authorModel, key, value)
        # Commit
        db.commit()
        db.refresh(authorModel)
    except NoResultFound:
        authorModel = None
    return authorModel


def delete_author(db, author_id: int, ):
    try:
        # Select del modelo ORM
        author = db.get(AuthorModel, author_id)
        db.delete(author)
        db.commit()
        authors = get_authors(db)
    except UnmappedInstanceError:
        authors = None
    return authors
