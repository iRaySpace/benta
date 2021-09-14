from pydantic import BaseModel

class Bin(BaseModel):
    id: int
    item: str
    qty: float
