from typing import Union, List
from pydantic import BaseModel


# Schemas de Podcasts
class PodcastBaseSchema(BaseModel):
    title: str
    description: str
    url: str
    category_id: int


class PodcastCreateSchema(PodcastBaseSchema):
    pass


class PodcastUpdateSchema(BaseModel):
    title: Union[str, None] = None
    description: Union[str, None] = None
    url: Union[str, None] = None


class PodcastSchema(PodcastBaseSchema):
    id: int

    class Config:
        orm_mode = True


class Author(BaseModel):
    id: int
    name: str
    nationality: str


class PodcastAuthorsSchema(PodcastSchema):
    authors: List[Author]


class AuthorPodcastsSchema(Author):
    podcasts: List[PodcastSchema]
