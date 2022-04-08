from typing import Optional

from manga_parser.schemas.remanga.contacts import Contacts
from manga_parser.schemas.remanga.image import ImageHigh, ImageLow, ImageMiddle
from manga_parser.schemas.remanga.pubisher_type import PublisherType
from manga_parser.schemas.remanga.rank import Rank
from manga_parser.schemas.remanga.subscription import Subscription
from pydantic import BaseModel, Field


class Publisher(BaseModel):
    # like 891
    id: int = Field(...)
    # like "891"
    short_url: str = Field(...)
    # like "https://remanga.org/team/891"
    url: str = Field(...)


class PublisherMedium(Publisher):
    # like "ArticaProject"
    name: str = Field(...)
    # like "Всё что мы делаем - это поступок..."
    short_description: Optional[str] = Field(...)
    publisher_type: PublisherType = Field(...)
    image: ImageLow = Field(...)


class PublisherHigh(PublisherMedium):
    description: Optional[str] = Field(...)
    images: tuple[ImageLow, ImageMiddle, ImageHigh] = Field(...)
    rank: Rank = Field(...)
    liked: int = Field(...)
    count_titles: int = Field(...)
    chapters_per_month: int = Field(...)
    contacts: Contacts = Field(...)
    subscription: Optional[Subscription] = Field(...)
