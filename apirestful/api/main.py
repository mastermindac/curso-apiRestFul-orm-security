from fastapi import FastAPI
from api import categoriesrouter, podcastsrouter, authorsrouter
from api import tags_metadata
from fastapi.middleware.cors import CORSMiddleware

#Origins permitidos politica CORS
origins = [
    "http://127.0.0.1:5500"
]

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Importacion de las rutas
app.include_router(
    categoriesrouter,
    tags=["categories"],
    prefix="/categories")

app.include_router(
    podcastsrouter,
    tags=["podcasts"],
    prefix="/podcasts")

app.include_router(
    authorsrouter,
    tags=["authors"],
    prefix="/authors")

@app.get("/")
async def root():
    return {"message": "Hola Pakito"}