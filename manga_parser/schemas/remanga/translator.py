from typing import Dict

from pydantic import BaseModel, Field


class Translator(BaseModel):
    """
    This object represents a translator.
    """

    name: str = Field(
        description="The translator's name",
    )
    short_description: str = Field(
        alias="tagline",
        description="The translator's short description",
    )
    description: str = Field(
        description="The translator's description",
    )
    short_url: str = Field(
        alias="dir",
        description="The translator's short url",
    )
    url: str = Field(
        description="The translator's url",
    )
    photo: str = Field(
        alias="img",
        description="The translator's photo",
    )
    rank: str = Field(
        description="The translator's rank",
    )
    count_works: int = Field(
        alias="count_titles",
        description="The translator's count works",
    )
    liked: int = Field(
        alias="count_votes",
        description="The number of likes on the chapters of all works",
    )
    chapters_month: int = Field(
        alias="count_period_chapters",
        description="Average number of chapters per month",
    )
    contacts: Dict[str, str] = Field(
        alias="links",
        description=(
            "The translator's contacts, such as: "
            "vk, youtube, fb, twitter, insta, discord"
        ),
    )
