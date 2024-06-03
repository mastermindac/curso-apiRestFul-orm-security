from sqlalchemy import create_engine, Column, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Creacion del Engine contra la BBDD
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root@localhost/masterpodcast'
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Genero la Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declarative base class
class Base(DeclarativeBase):
    pass

#Tabla asociacion entre podcasts y  author
podcast_authors= Table(
    "podcast_authors",
    Base.metadata,
    Column("podcast_id", ForeignKey("podcasts.id"), primary_key=True),
    Column("author_id", ForeignKey("authors.id"), primary_key=True),
)


# Dependency
def get_db():
    # Creando la Session
    db = SessionLocal()
    # Intentado devolver la sesion
    try:
        # Devolvemos la sesion
        yield db
    finally:
        # Cerrar sesion al finalizar el proceso
        db.close()
