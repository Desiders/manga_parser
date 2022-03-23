from pydantic import BaseModel, Field


class Genre(BaseModel):
    id: int = Field(...)
    # like "боевик", "боевые искусства, etc.
    value: str = Field(...)
