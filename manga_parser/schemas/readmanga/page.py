from pydantic import BaseModel, Field


class Page(BaseModel):
    """
    This object represents a page of the chapter.
    """

    url: str = Field(
        description="The page's url",
    )
    width: int = Field(
        description="The page's width",
    )
    height: int = Field(
        description="The page's height",
    )
