"""API v1 routes"""

from fastapi import APIRouter, HTTPException
from src.models.schemas import Item, ItemCreate, ItemUpdate
from typing import List

router = APIRouter()

# Mock database storage
items_db: dict = {}
item_counter = 0


@router.get("/items", response_model=List[Item])
async def get_items(skip: int = 0, limit: int = 10):
    """Get all items with pagination"""
    items = list(items_db.values())
    return items[skip : skip + limit]


@router.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """Get a specific item by ID"""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]


@router.post("/items", response_model=Item)
async def create_item(item: ItemCreate):
    """Create a new item"""
    global item_counter
    item_counter += 1
    item_data = item.dict()
    item_data["id"] = item_counter
    items_db[item_counter] = item_data
    return item_data


@router.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: ItemUpdate):
    """Update an existing item"""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    update_data = item.dict(exclude_unset=True)
    items_db[item_id].update(update_data)
    return items_db[item_id]


@router.delete("/items/{item_id}")
async def delete_item(item_id: int):
    """Delete an item"""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return {"message": "Item deleted successfully"}
