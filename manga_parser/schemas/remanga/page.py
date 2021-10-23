from pydantic import BaseModel, Field


class Page(BaseModel):
    """
    This object represents a page of the chapter.
    """

    url: str = Field(
        alias="link",
        description="The page's url",
    )
    height: int = Field(
        description="The page's height",
    )
    width: int = Field(
        description="The page's width",
    )
    count_comments: int = Field(
        description="The number comments of the page",
    )
