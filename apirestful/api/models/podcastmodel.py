from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from api import Base



# Modelo Podcast
class Podcast(Base):
    __tablename__ = "podcasts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    url: Mapped[str]
    # Relacion One-To-Many categories
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
