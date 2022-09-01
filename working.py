from fastapi import FastAPI, Path, Query, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

inventory = {}

@app.get("/get-item/{item_id}")
def home(item_id: int = Path(None, description="The Id of the Item would you like", gt=0)):
    return inventory[item_id]

@app.get("/get-by-name")
def home(name: str = Query(None, title="Name", description="Name of the item", max_length=10, min_length=2)):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data": "Not found"}

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item Id already exists"}

    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update-item/{item-id}")
def update_item(item_id: int, item: Item):
    if item_id not in inventory:
        return {"Error": "Item dose not exists"}

    if item.name is not None:
        inventory[item_id].name = item.name

    if item.price is not None:
        inventory[item_id].price = item.price

    if item.brand is not None:
        inventory[item_id].brand = item.brand

    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="The Id of the Item to delete", gt=0)):
    if item_id not in inventory:
        return {"Error": "Id dose not exist"}

    del inventory[item_id]
    return {"Success": "Item deleted"}
