import time
from typing import Optional, Union

from fastapi import Body, FastAPI
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
app = FastAPI()


class Item(BaseModel):
    name: str
    price: float = None
    is_offer: Union[bool, None] = None


while(True):
    try:
        conn = psycopg2.connect(
            host='localhost', database='fastapi', user='postgres', password='', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("database connection was successful")
        break
    except Exception as error:
        print("Database connection failed")
        print(error)
        time.sleep(2)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/")
def post_item(item: Item):
    print(item.price)
    return {"Item": "Posted"}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_price": item.price, "item_id": item_id}
