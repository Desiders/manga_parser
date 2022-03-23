from pydantic import BaseModel, Field


# <- manga_parser.utils.remanga.genre_by_id
class Genre(BaseModel):
    id: int = Field(...)
    # like "боевик", "боевые искусства, etc.
    value: str = Field(...)
