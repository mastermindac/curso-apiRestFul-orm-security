from api.database.database import engine, get_db, SessionLocal

# Configuracion de la documentacion
from api.configdoc import tags_metadata

# Modelos DB
from api.database.database import Base
from api.database.database import podcast_authors
from api.models.categorymodel import Category as CategoryModel
from api.models.podcastmodel import Podcast as PodcastModel
from api.models.authormodel import Author as AuthorModel

# Schemas Pydantic
from api.schemas.authorschema import AuthorSchema, AuthorCreateSchema, AuthorUpdateSchema
from api.schemas.podcastschema import PodcastSchema, PodcastCreateSchema, PodcastUpdateSchema, PodcastAuthorCreateSchema
from api.schemas.podcastschema import PodcastAuthorsSchema, AuthorPodcastsSchema
from api.schemas.categoryschema import CategorySchema, CategoryPodcastsSchema, CategoryCreateSchema


# Controladores
from api.controllers import categorycontroller
from api.controllers import podcastcontroller
from api.controllers import authorcontroller

# Rutas
from api.routers.categories import router as categoriesrouter
from api.routers.podcasts import router as podcastsrouter
from api.routers.authors import router as authorsrouter

# App
from api.main import app
