from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Creacion del Engine contra la BBDD
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root@localhost/masterpodcast'
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Genero la Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declarative base class
class Base(DeclarativeBase):
    pass


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
