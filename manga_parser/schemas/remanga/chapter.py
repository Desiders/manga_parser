from typing import List, Optional

from pydantic import BaseModel, Field


class Chapter(BaseModel):
    """
    This object represents a chapter of the manga.
    """

    name: Optional[str] = Field(
        description="The chapter's name",
    )
    id: int = Field(
        description="The chapter's id",
    )
    tome: int = Field(
        description="The chapter of the volume",
    )
    chapter: float = Field(
        description="The chapter's numeric identifier, for example 23.3",
    )
    index: int = Field(
        description=(
            "The chapter's numeric value, "
            "for example index 2, is 1.1, because index 1 is chapter 1.0"
        ),
    )
    liked: int = Field(
        alias="score",
        description="The number of likes on chapter",
    )
    is_free: bool = Field(
        description="The chapter is free",
    )
    price: Optional[float] = Field(
        description=(
            "The chapter's price. "
            "The price may be even if the chapter is free"
        ),
    )
    free_date: Optional[str] = Field(
        alias="pub_date",
        description="The date when the chapter became or will be free"
    )
    date: str = Field(
        alias="upload_date",
        description="The chapter's release date",
    )
    translators: List[str] = Field(
        alias="publishers",
        description="The translators' names of the chapter",
    )
