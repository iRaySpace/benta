from pydantic import BaseModel

class Warehouse(BaseModel):
    id: int
    name: str
