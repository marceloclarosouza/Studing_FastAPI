from pydantic import BaseModel
from typing import Optional

import databases
import sqlalchemy

DATABASE_URL = "sqlite:///fastapidb.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

items = sqlalchemy.Table(
    "items",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("product", sqlalchemy.String),
    sqlalchemy.Column("price", sqlalchemy.Float),
    sqlalchemy.Column("stock", sqlalchemy.Integer),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)


class ItemPost(BaseModel):
    product: str
    price: float
    stock: int

class ItemGet(BaseModel):
    id: int
    product: str
    price: float
    stock: int
    