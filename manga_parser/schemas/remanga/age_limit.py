from pydantic import BaseModel, Field


class AgeLimit(BaseModel):
    id: int = Field(...)
    # 0+, 16+, 18+
    value: str = Field(...)
