from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Starter FastAPI CRUD")


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


# In-memory storage
items: List[Item] = []


@app.get("/items", response_model=List[Item])
def list_items():
    return items


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    # simple check for duplicate id
    if any(i.id == item.id for i in items):
        raise HTTPException(status_code=400, detail="Item with this id already exists")
    items.append(item)
    return item


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for it in items:
        if it.id == item_id:
            return it
    raise HTTPException(status_code=404, detail="Item not found")


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    for idx, it in enumerate(items):
        if it.id == item_id:
            items[idx] = item
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for idx, it in enumerate(items):
        if it.id == item_id:
            items.pop(idx)
            return {"detail": "deleted"}
    raise HTTPException(status_code=404, detail="Item not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("starter_server:app", host="127.0.0.1", port=8000, reload=True)
