from sqlmodel import create_engine,Session

# Creacion del Engine contra la BBDD
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root@localhost/masterpodcast'
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Dependency
def get_db():
    # Creando la Session
    db = Session(engine)
    # Intentado devolver la sesion
    try:
        # Devolvemos la sesion
        yield db
    finally:
        # Cerrar sesion al finalizar el proceso
        db.close()
