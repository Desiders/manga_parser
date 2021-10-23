from typing import List, Optional

from pydantic import BaseModel, Field

from .translator_briefly import TranslatorBriefly


class Branch(BaseModel):
    """
    This object represents a branch.
    """

    id: int = Field(
        description="The branch's id",
    )
    photo: Optional[str] = Field(
        alias="img",
        description="The branch's photo",
    )
    translators: List[TranslatorBriefly] = Field(
        alias="publishers",
        description="The branch's translators",
    )
    liked: int = Field(
        alias="total_votes",
        description="The number of likes on chapters in this branch",
    )
    count_chapters: int = Field(
        description="The number chapters of the manga in this branch",
    )
