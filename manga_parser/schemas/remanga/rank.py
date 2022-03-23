from pydantic import BaseModel, Field


# <- manga_parser.utils.remanga.rank_by_id
class Rank(BaseModel):
    id: int = Field(...)
    # "золотой", "серебряный", "бронзовый", "деревянный"
    name: str = Field(...)
