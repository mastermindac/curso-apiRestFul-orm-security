from typing import List

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from api import Base, podcast_authors



# Modelo Podcast
class Podcast(Base):
    __tablename__ = "podcasts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    url: Mapped[str]
    # Relacion One-To-Many categories
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    #Relacion many to many authors
    authors: Mapped[List["Author"]] = relationship(
        secondary=podcast_authors, back_populates="podcasts"
    )
