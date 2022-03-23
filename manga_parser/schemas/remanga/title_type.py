from pydantic import BaseModel, Field


# <- manga_parser.utils.remanga.title_type_by_id
class TitleType(BaseModel):
    id: int = Field(...)
    # "manga", "manhwa", "manhua", "comics", etc.
    en_value: str = Field(...)
    # "манга", "манхва", "маньхуа", "западный комикс", etc.
    ru_value: str = Field(...)
