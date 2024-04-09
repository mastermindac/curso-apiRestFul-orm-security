from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy import text

#Creacion del Engine contra la BBDD
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root@localhost/masterpodcast'
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

#Debug
#comprobamos la correcta conexion
#with engine.connect() as connection:
#    result = connection.execute(text("select name from categories"))
#    for row in result:
#        print("nombre:", row.name)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hola Pakito"}