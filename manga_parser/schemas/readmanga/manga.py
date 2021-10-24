from typing import List, Optional

from pydantic import BaseModel, Field

from .chapter import Chapter
from .manga_briefly import MangaBriefly
from .translator_briefly import TranslatorBriefly


class Manga(BaseModel):
    """
    This object represents a manga.
    """

    name: str = Field(
        description="The manga's name",
    )
    short_url: str = Field(
        description="The manga's short url",
    )
    url: str = Field(
        description="The manga's url",
    )
    description: str = Field(
        description="The manga's description",
    )
    photo: List[str] = Field(
        description="Main the manga's photos",
    )
    votes: int = Field(
        alias="ratingCount",
        description="The number of votes to evaluate the manga",
    )
    stars: float = Field(
        alias="ratingValue",
        description="The manga's rating",
    )
    status: str = Field(
        description="The chapter's exit status",
    )
    year: int = Field(
        alias="elem_year",
        description="Year of release of the manga",
    )
    category: Optional[str] = Field(
        default=None,
        alias="elem_category",
        description="The manga's category (manga/manhua/manhwa)",
    )
    tags: List[str] = Field(
        description="Tags and genres of the manga",
    )
    authors: List[str] = Field(
        default=[],
        alias="elem_author",
        description="Authors of the manga",
    )
    screenwriters: List[str] = Field(
        default=[],
        alias="elem_screenwriter",
        description="Screenwriters of the manga",
    )
    illustrators: List[str] = Field(
        default=[],
        alias="elem_illustrator",
        description="Illustrators of the manga",
    )
    publishers: List[str] = Field(
        default=[],
        alias="elem_publisher",
        description="Publishers of the manga",
    )
    translators: List[TranslatorBriefly] = Field(
        default=[],
        alias="elem_translator",
        description="Translators of the manga",
    )
    chapters: List[Chapter] = Field(
        default=[],
        description="The manga's chapters",
    )
    count_chapters: int = Field(
        default=0,
        description="The number chapters of the manga in this branch",
    )
    similar: List[MangaBriefly] = Field(
        default=[],
        description="The similar manga",
    )
