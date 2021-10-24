from pydantic import BaseModel, Field


class MangaBriefly(BaseModel):
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
    photo: str = Field(
        description="The manga's photo",
    )
