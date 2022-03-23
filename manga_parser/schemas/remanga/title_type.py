from pydantic import BaseModel, Field


class TitleType(BaseModel):
    id: int = Field(...)
    # "manga", "manhwa", "manhua", "comics", etc.
    en_value: str = Field(...)
    # "манга", "манхва", "маньхуа", "западный комикс", etc.
    ru_value: str = Field(...)
