# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from database_sqlite import SQLiteDatabase

app = FastAPI()
db = SQLiteDatabase("items.db")

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: str
    price: float

@app.get("/items/", response_model=List[Item])
async def get_items():
    return db.get_all()

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    item = db.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return db.create(item.dict(exclude={'id'}))

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    updated_item = db.update(item_id, item.dict(exclude={'id'}))
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    success = db.delete(item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}