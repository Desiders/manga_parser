from pydantic import BaseModel, Field


class TranslatorBriefly(BaseModel):
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
    short_url: str = Field(
        alias="dir",
        description="The translator's short url",
    )
    url: str = Field(
        description="The translator's url",
    )
