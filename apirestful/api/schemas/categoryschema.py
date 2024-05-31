from typing import Union, List
from pydantic import BaseModel

from api import PodcastSchema


#Schemas de Categoria
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

class CategoryPodcasts(CategoryBase):
    id: int
    podcasts: List[PodcastSchema]

    class Config:
        orm_mode = True