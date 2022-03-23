from pydantic import BaseModel, Field


# <- manga_parser.utils.remanga.publisher_type_by_id
# <- manga_parser.utils.remanga.publisher_type_by_type
class PublisherType(BaseModel):
    # "переводчик", "автор", "издатель"
    en_value: str = Field(...)
    # "translator", "author", "publisher"
    ru_value: str = Field(...)
