from typing import Optional
from pydantic import BaseModel, Field


class Contacts(BaseModel):
    # like "https://vk.com/articaproject"
    vk: Optional[str] = Field(...)
    facebook: Optional[str] = Field(...)
    youtube: Optional[str] = Field(...)
    twitter: Optional[str] = Field(...)
    instagram: Optional[str] = Field(...)
    discord: Optional[str] = Field(...)
