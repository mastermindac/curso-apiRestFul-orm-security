from typing import Union
from pydantic import BaseModel

#Schemas de Podcasts
class AuthorBase(BaseModel):
    name: str
    nationality: str

class AuthorCreate(AuthorBase):
    pass

class AuthorUpdate(BaseModel):
    name: Union[str, None] = None
    nationality: Union[str, None] = None

class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True