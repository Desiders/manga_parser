from typing import Optional

from manga_parser.schemas.remanga.age_limit import AgeLimit
from manga_parser.schemas.remanga.branch import Branch
from manga_parser.schemas.remanga.category import Category
from manga_parser.schemas.remanga.genre import Genre
from manga_parser.schemas.remanga.image import ImageHigh, ImageLow, ImageMiddle
from manga_parser.schemas.remanga.publisher import PublisherMedium
from manga_parser.schemas.remanga.status import Status
from manga_parser.schemas.remanga.title_type import TitleType
from pydantic import BaseModel, Field


class Manga(BaseModel):
    # like 938
    id: int = Field(...)


class MangaBriefly(Manga):
    # like "The Beginning After the End"
    en_name: str = Field(...)
    # like "Начало после конца"
    ru_name: str = Field(...)
    # "the_beginning_after_the_end"
    short_url: str = Field(...)
    # like "https://remanga.org/api/titles/the_beginning_after_the_end"
    url: str = Field(...)
    title_type: TitleType = Field(...)
    images: tuple[ImageLow, ImageMiddle, ImageHigh] = Field(...)
    # like 2018
    issue_year: Optional[int] = Field(...)
    # like 9.5
    rating: float = Field(...)
    # like 136
    count_chapters: int = Field(...)


# this class cannot be a child of 'Manga Briefly',
# because it doesn't have `count_chapters` attribute.
class MangaMedium(Manga):
    # like "The Beginning After the End"
    en_name: str = Field(...)
    # like "Начало после конца"
    ru_name: str = Field(...)
    # "the_beginning_after_the_end"
    short_url: str = Field(...)
    # like "https://remanga.org/api/titles/the_beginning_after_the_end"
    url: str = Field(...)
    title_type: TitleType = Field(...)
    images: tuple[ImageLow, ImageMiddle, ImageHigh] = Field(...)
    # like 2018
    issue_year: Optional[int] = Field(...)
    # like 9.5
    rating: float = Field(...)
    # like 2206093
    liked: int = Field(...)
    # like 10078394
    views: int = Field(...)
    genres: list[Genre] = Field(...)
    categories: list[Category] = Field(...)


class MangaHigh(MangaMedium):
    # like "끝이 아닌 시작"
    another_name: str = Field(...)
    # like 136
    count_chapters: int = Field(...)
    # like 17304
    votes: int = Field(...)
    # like 125054
    bookmarks: int = Field(...)
    # like "Король Грей обладает..."
    description: Optional[str] = Field(...)
    status: Status = Field(...)
    age_limit: AgeLimit = Field(...)
    publishers: list[PublisherMedium] = Field(...)
    branches: list[Branch] = Field(...)
