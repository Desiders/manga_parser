from pydantic import BaseModel, Field


# <- manga_parser.utils.remanga.age_limit_by_id
class AgeLimit(BaseModel):
    id: int = Field(...)
    # 0+, 16+, 18+
    value: str = Field(...)
