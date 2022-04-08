from pydantic import BaseModel, Field


class Genre(BaseModel):
    # like "action", "martial_arts", etc.
    en_value: str = Field(...)
    # like "боевик", "боевые искусства, etc.
    ru_value: str = Field(...)
