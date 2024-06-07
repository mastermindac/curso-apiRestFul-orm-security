from typing import Union, List
from pydantic import BaseModel


# Schemas de Podcasts
class PodcastBaseSchema(BaseModel):
    title: str
    description: str
    url: str
    category_id: int


class PodcastUpdateSchema(BaseModel):
    title: Union[str, None] = None
    description: Union[str, None] = None
    url: Union[str, None] = None


class PodcastSchema(PodcastBaseSchema):
    id: int

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    id: int


class Author(AuthorBase):
    name: str
    nationality: str


class PodcastAuthorCreateSchema(BaseModel):
    authors: List[AuthorBase]


class PodcastCreateSchema(PodcastBaseSchema):
    authors: List[AuthorBase]


class PodcastAuthorsSchema(PodcastSchema):
    authors: List[Author]


class AuthorPodcastsSchema(Author):
    podcasts: List[PodcastSchema]
