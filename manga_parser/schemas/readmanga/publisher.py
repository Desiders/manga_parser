from pydantic import BaseModel, Field


class Publisher(BaseModel):
    pass


class PublisherBriefly(Publisher):
    name: str = Field(...)
    short_url: str = Field(...)
    url: str = Field(...)
