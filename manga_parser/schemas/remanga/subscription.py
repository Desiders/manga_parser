from pydantic import BaseModel, Field


class Subscription(BaseModel):
    # like 231
    id: int = Field(...)
    # like "AssleyVIP"
    name: str = Field(...)
    # like "Для приобретения пишите в группу вк"
    description: str = Field(...)
    # like 300.0
    price: float = Field(...)
    # like "1 месяц"
    period: str = Field(...)
