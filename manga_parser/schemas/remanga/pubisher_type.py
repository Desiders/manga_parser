from pydantic import BaseModel, Field


class PublisherType(BaseModel):
    # "переводчик", "автор", "издатель"
    en_value: str = Field(...)
    # "translator", "author", "publisher"
    ru_value: str = Field(...)
