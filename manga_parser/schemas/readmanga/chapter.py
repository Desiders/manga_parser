from typing import Optional

from pydantic import BaseModel, Field


class Chapter(BaseModel):
    """
    This object represents a chapter of the manga.
    """

    name: str = Field(
        description="The chapter's name",
    )
    url: str = Field(
        description="The chapter's url",
    )
    translator: Optional[str] = Field(
        default=None,
        description="The translator's name",
    )
    date: str = Field(
        description="The chapter's release date",
    )
