import sqlalchemy
import psycopg2

from fastapi import FastAPI
from models import ItemGet, ItemPost, database, items
from typing import List

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()    

@app.get("/items/", response_model=List[ItemGet])
async def read_items():
    query = items.select()
    return await database.fetch_all(query)
    
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     query = items.select()
#     return await {"item_id": item_id}

@app.post("/items/", response_model=ItemGet)
async def create_item(item: ItemPost):
    query = items.insert().values(product=item.product,
                                  price=item.price,
                                  stock=item.stock)
    last_record_id = await database.execute(query)
    return {**item.dict(), "id": last_record_id}
