from pydantic import BaseModel, Field


class Status(BaseModel):
    id: int = Field(...)
    # "completed", "ongoing", "hiatus", "no translator", etc.
    en_value: str = Field(...)
    # "завершено", "продолжается", "заморожен", "нет переводчика", etc.
    ru_value: str = Field(...)
