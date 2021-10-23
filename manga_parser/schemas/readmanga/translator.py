from typing import List, Optional

from pydantic import BaseModel, Field

from .manga_briefly import MangaBriefly


class Translator(BaseModel):
    """
    This object represents a translator.
    """

    name: str = Field(
        description="The translator's name",
    )
    name_en: Optional[str] = Field(
        default=None,
        alias="eng-name",
        description="The translator's name in English",
    )
    original_name: Optional[str] = Field(
        default=None,
        alias="original-name",
        description="The translator's original name",
    )
    votes: int = Field(
        alias="ratingCount",
        description="The number of votes to evaluate the translator",
    )
    stars: float = Field(
        alias="ratingValue",
        description="The translator's rating",
    )
    description: Optional[str] = Field(
        default=None,
        alias="manga-description",
        description="The translator's description",
    )
    short_url: str = Field(
        description="The translator's short url",
    )
    url: str = Field(
        description="The translator's url",
    )
    date_create: Optional[str] = Field(
        default=None,
        alias="birthDate",
        description="Team creation date",
    )
    contact: Optional[str] = Field(
        default=None,
        description="The translator's contact",
    )
    works: List[MangaBriefly] = Field(
        default=[],
        description="The author's works",
    )
