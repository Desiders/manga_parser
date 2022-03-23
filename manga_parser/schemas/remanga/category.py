from pydantic import BaseModel, Field


# <- manga_parser.utils.remanga.category_by_id
class Category(BaseModel):
    id: int = Field(...)
    # "веб", "в цвете", "ёнкома", "сборник", etc.
    value: str = Field(...)
