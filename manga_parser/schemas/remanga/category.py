from pydantic import BaseModel, Field


class Category(BaseModel):
    id: int = Field(...)
    # "веб", "в цвете", "ёнкома", "сборник", etc.
    value: str = Field(...)
