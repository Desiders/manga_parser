from pydantic import BaseModel, Field


class TranslatorBriefly(BaseModel):
    """
    This object represents a translator.
    """

    name: str = Field(
        description="The translator's name",
    )
    short_url: str = Field(
        description="The translator's short url",
    )
    url: str = Field(
        description="The translator's url",
    )
