from pydantic import BaseModel, Field


class Image(BaseModel):
    url: str = Field(...)
    # like 130
    width: int = Field(...)
    # like 180
    height: int = Field(...)


class ImageLow(Image):
    pass
