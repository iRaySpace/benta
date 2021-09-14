from pydantic import BaseModel
from fastapi import FastAPI
from fastapi_crudrouter import MemoryCRUDRouter as CRUDRouter
from benta.models.bin import Bin

app = FastAPI()
app.include_router(CRUDRouter(schema=Bin))
