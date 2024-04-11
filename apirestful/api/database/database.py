from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Creacion del Engine contra la BBDD
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root@localhost/masterpodcast'
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
