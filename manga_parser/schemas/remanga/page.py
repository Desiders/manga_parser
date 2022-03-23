from pydantic import BaseModel, Field


class Page(BaseModel):
    # like 2220228
    id: int = Field(...)
    # like "https://img5.reimg.org/images/111/2-13/2_re.jpg"
    url: str = Field(...)
    # like 1298
    height: int = Field(...)
    # like 900
    width: int = Field(...)
    # like 0
    count_comments: int = Field(...)
