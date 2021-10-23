from typing import List, Optional

from pydantic import BaseModel, Field

from .branch import Branch
from .translator_briefly import TranslatorBriefly


class Manga(BaseModel):
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
    description: str = Field(
        description="The manga's description",
    )
    photo: str = Field(
        alias="img",
        description="The manga's photo",
    )
    votes: int = Field(
        alias="count_rating",
        description="The number of votes to evaluate the manga",
    )
    stars: float = Field(
        alias="avg_rating",
        description="The manga's rating",
    )
    saved: int = Field(
        alias="count_bookmarks",
        description="The number of saved manga",
    )
    liked: int = Field(
        alias="total_votes",
        description="The number of likes on chapters",
    )
    views: int = Field(
        alias="total_views",
        description="The number of manga views",
    )
    status: str = Field(
        description="The chapter exit status",
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
    translators: Optional[List[TranslatorBriefly]] = Field(
        alias="publishers",
        description="Translators of the manga",
    )
    branches: List[Branch] = Field(
        description=(
            "The manga's branches. "
            "A lot of translators can work on the manga"
        ),
    )
    count_chapters: int = Field(
        description="The number chapters of the manga",
    )
