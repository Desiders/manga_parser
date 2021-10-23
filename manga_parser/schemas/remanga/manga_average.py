from typing import List, Optional

from pydantic import BaseModel, Field


class MangaAverage(BaseModel):
    """
    This object represents a manga.
    """

    name_ru: str = Field(
        alias="rus_name",
        description="The manga's name in Russian",
    )
    name_en: str = Field(
        alias="en_name",
        description="The manga's name in English",
    )
    short_url: str = Field(
        alias="dir",
        description="The manga's short url",
    )
    url: str = Field(
        description="The manga's url",
    )
    id: int = Field(
        description="The manga's id",
    )
    photo: str = Field(
        alias="img",
        description="The manga's photo",
    )
    stars: float = Field(
        alias="avg_rating",
        description="The manga's rating",
    )
    liked: int = Field(
        alias="total_votes",
        description="The number of likes on chapters",
    )
    views: int = Field(
        alias="total_views",
        description="The number of manga views",
    )
    year: Optional[int] = Field(
        alias="issue_year",
        description="Year of release of the manga",
    )
    category: str = Field(
        alias="type",
        description="The manga category (manga/manhua/manhwa)",
    )
    tags: List[str] = Field(
        alias="genres",
        description="Tags and genres of the manga",
    )
    count_chapters: int = Field(
        description="The number chapters of the manga",
    )
