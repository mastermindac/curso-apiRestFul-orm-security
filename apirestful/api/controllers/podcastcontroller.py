from sqlalchemy import select
from api import PodcastModel, PodcastCreateSchema, PodcastUpdateSchema
from sqlalchemy.exc import NoResultFound, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError


# Controller de podcasts
def get_podcasts(db):
    try:
        # Crearia la consulta SELECT * from categories
        stmt = select(PodcastModel)
        # Lista de categorias
        result = db.scalars(stmt)
        podcasts = result.all()
    except OperationalError:
        podcasts = None
    return podcasts


def get_podcast(db, podcast_id: int):
    try:
        # Select del modelo ORM
        result = db.execute(select(PodcastModel).filter_by(id=podcast_id))
        podcastModel = result.scalar_one()
    except NoResultFound:
        podcastModel = None
    return podcastModel


def write_podcast(db, podcast: PodcastCreateSchema):
    # Crearemos el modelo ORM a partir del Schema
    podcastModel = PodcastModel(title=podcast.title, description=podcast.description , url=podcast.url, category_id=podcast.category_id)
    # Insertamos en la DB
    db.add(podcastModel)
    # Commit
    db.commit()
    db.refresh(podcastModel)
    return podcastModel


def update_podcast(db, podcast_id: int, podcast: PodcastUpdateSchema):
    try:
        # Select del modelo ORM
        result = db.execute(select(PodcastModel).filter_by(id=podcast_id))
        podcastModel = result.scalar_one()
        # Modificamos el podcast
        # Update model class variable from requested fields
        for key, value in podcast:
            if value is not None: setattr(podcastModel, key, value)
        # Commit
        db.commit()
        db.refresh(podcastModel)
    except NoResultFound:
        podcastModel = None
    return podcastModel


def delete_podcast(db, podcast_id: int, ):
    try:
        # Select del modelo ORM
        podcast = db.get(PodcastModel, podcast_id)
        db.delete(podcast)
        db.commit()
        podcasts = get_podcasts(db)
    except UnmappedInstanceError:
        podcasts = None
    return podcasts
