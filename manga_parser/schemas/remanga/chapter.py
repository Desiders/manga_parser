from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Chapter(BaseModel):
    # like 598919
    id: int = Field(...)
    # like 5
    tome: int = Field(...)
    # like 8.1
    chapter_number: float = Field(...)
    # like 137
    chapter_index: int = Field(...)
    # like "То, за что я сражаюсь"
    name: str = Field(...)
    # like 902
    liked: int = Field(...)
    # True, False
    is_paid: bool = Field(...)
    # like 15.0
    price: Optional[float] = Field(...)
    upload_date: datetime = Field(...)
    free_date: Optional[datetime] = Field(...)
