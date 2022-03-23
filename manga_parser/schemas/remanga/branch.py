from manga_parser.schemas.remanga.image import ImageLow
from manga_parser.schemas.remanga.publisher import PublisherHigh
from pydantic import BaseModel, Field


class Branch(BaseModel):
    # like 852
    id: int = Field(...)
    image: ImageLow = Field(...)
    # like 2206093
    liked: int = Field(...)
    # like 136
    count_chapters: int = Field(...)
    publishers: list[PublisherHigh] = Field(...)
