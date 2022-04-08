from typing import Optional

from manga_parser.schemas.readmanga.genre import Genre
from manga_parser.schemas.readmanga.image import ImageLow
from manga_parser.schemas.readmanga.publisher import PublisherBriefly
from pydantic import BaseModel, Field


class Manga(BaseModel):
    # like "Танджиро - старший сын в семье, потерявшей кормильца..."
    short_url: str = Field(...)
    # like "https://readmanga.io/klinok__rassekaiuchii_demonov__A5327"
    url: str = Field(...)


class MangaBriefly(Manga):
    # like "Клинок, рассекающий демонов"
    ru_name: str = Field(...)
    # like "klinok__rassekaiuchii_demonov__A5327"
    description: str = Field(...)
    image: Optional[ImageLow] = Field(...)
    publisher: Optional[PublisherBriefly] = Field(...)
    genres: list[Genre] = Field(...)
