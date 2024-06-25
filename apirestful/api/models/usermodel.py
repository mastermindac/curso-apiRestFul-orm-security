from typing import List

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from api import Base, podcast_authors


# Modelo Podcast
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]
    name: Mapped[str]
    active: Mapped[bool]