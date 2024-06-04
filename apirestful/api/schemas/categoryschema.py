from typing import Union, List
from pydantic import BaseModel

from api import PodcastSchema


# Schemas de Categoria
class CategoryBaseSchema(BaseModel):
    name: str


class CategoryCreateSchema(CategoryBaseSchema):
    pass


class CategorySchema(CategoryBaseSchema):
    id: int


class CategoryPodcastsSchema(CategoryBaseSchema):
    id: int
    podcasts: List[PodcastSchema]

    class Config:
        orm_mode = True
