from api.database.database import engine, get_db, SessionLocal

# Configuracion de la documentacion
from api.configdoc import tags_metadata

# Modelos DB
from api.models.categorymodel import Category as CategoryModel
from api.models.podcastmodel import Podcast as PodcastModel
from api.models.authormodel import Author as AuthorModel

# Schemas Pydantic
from api.schemas.categoryschema import Category as CategorySchema
from api.schemas.categoryschema import CategoryCreate as CategoryCreateSchema
from api.schemas.podcastschema import Podcast as PodcastSchema
from api.schemas.podcastschema import PodcastCreate as PodcastCreateSchema
from api.schemas.podcastschema import PodcastUpdate as PodcastUpdateSchema
from api.schemas.authorschema import Author as AuthorSchema
from api.schemas.authorschema import AuthorCreate as AuthorCreateSchema
from api.schemas.authorschema import AuthorUpdate as AuthorUpdateSchema

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
