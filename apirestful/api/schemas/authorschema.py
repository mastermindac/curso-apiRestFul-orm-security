from typing import Union
from pydantic import BaseModel


# Schemas de Podcasts
class AuthorBaseSchema(BaseModel):
    name: str
    nationality: str


class AuthorCreateSchema(AuthorBaseSchema):
    pass


class AuthorUpdateSchema(BaseModel):
    name: Union[str, None] = None
    nationality: Union[str, None] = None


class AuthorSchema(AuthorBaseSchema):
    id: int

    class Config:
        orm_mode = True
