from pydantic import BaseModel, Field


class Image(BaseModel):
    url: str = Field(...)


class ImageLow(Image):
    # like "https://remanga.org/media/titles/the_beginning_after_the_end/
    # low_cover.jpg"
    pass


class ImageMiddle(Image):
    # like "https://remanga.org/media/titles/the_beginning_after_the_end/
    # mid_cover.jpg"
    pass


class ImageHigh(Image):
    # like "https://remanga.org/media/titles/the_beginning_after_the_end/
    # high_cover.jpg"
    pass
