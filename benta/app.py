from pydantic import BaseModel
from fastapi import FastAPI
from fastapi_crudrouter import MemoryCRUDRouter as CRUDRouter
from benta.models.bin import Bin
from benta.models.warehouse import Warehouse

app = FastAPI()
app.include_router(CRUDRouter(schema=Bin))
app.include_router(CRUDRouter(schema=Warehouse))
