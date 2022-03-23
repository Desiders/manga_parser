from pydantic import BaseModel, Field


class Image(BaseModel):
    pass


class ImageLow(Image):
    # like "https://remanga.org/media/titles/the_beginning_after_the_end/
    # low_cover.jpg"
    url: str = Field(...)


class ImageMiddle(Image):
    # like "https://remanga.org/media/titles/the_beginning_after_the_end/
    # mid_cover.jpg"
    url: str = Field(...)


class ImageHigh(Image):
    # like "https://remanga.org/media/titles/the_beginning_after_the_end/
    # high_cover.jpg"
    url: str = Field(...)
