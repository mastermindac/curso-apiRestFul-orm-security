from fastapi import FastAPI
from api import categoriesrouter
from api import tags_metadata

#Apirestful con FastApi
app = FastAPI(
    title="Mastermind Podcast API",
    description="ApiRestFul para la gestión de los podcast realizados por Mastermind",
    version="0.1",
    contact={
        "name": "Paco Gómez",
        "url": "http://www.mastermind.ac"
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata
)

#Importacion de las rutas
app.include_router(
    categoriesrouter,
    tags=["categories"],
    prefix="/categories")

@app.get("/")
async def root():
    return {"message": "Hola Pakito"}