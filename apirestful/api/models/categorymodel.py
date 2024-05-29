from typing import List

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from api import Base



# Modelo Category
class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    #Relacion One-To-Many podcasts
    podcasts: Mapped[List["Podcast"]] = relationship()
