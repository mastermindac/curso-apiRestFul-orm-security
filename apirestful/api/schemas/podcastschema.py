from typing import Union
from pydantic import BaseModel

#Schemas de Podcasts
class PodcastBase(BaseModel):
    title: str
    description: str
    url: str

class PodcastCreate(PodcastBase):
    pass

class PodcastUpdate(BaseModel):
    title: Union[str, None] = None
    description: Union[str, None] = None
    url: Union[str, None] = None

class Podcast(PodcastBase):
    id: int

    class Config:
        orm_mode = True