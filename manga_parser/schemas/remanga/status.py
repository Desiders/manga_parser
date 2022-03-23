from pydantic import BaseModel, Field


# <- manga_parser.utils.remanga.status_by_id
class Status(BaseModel):
    id: int = Field(...)
    # "completed", "ongoing", "hiatus", "no translator", etc.
    en_value: str = Field(...)
    # "завершено", "продолжается", "заморожен", "нет переводчика", etc.
    ru_value: str = Field(...)
