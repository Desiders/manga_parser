from pydantic import BaseModel, Field


class Rank(BaseModel):
    id: int = Field(...)
    # "золотой", "серебряный", "бронзовый", "деревянный"
    name: str = Field(...)
