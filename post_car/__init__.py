from pydantic import BaseModel


class PostCarModel(BaseModel):
    type: str
    brand: str
    model: str
    wearness: str
    trader_number: int
    cost: int

