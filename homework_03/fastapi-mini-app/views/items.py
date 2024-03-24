from fastapi import APIRouter, Path, Body
from typing import Annotated
from pydantic import BaseModel

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/")
def get_items_list():
    return {
        "data": [
            {"id": 1, "name": "Item 1"},
            {"id": 2, "name": "Item 2"},
        ]
    }


class ItemCreate(BaseModel):
    name: str
    description: str


@router.get("/{item_id}")
def get_item(
        item_id: Annotated[int, Path(lt=1_000_000, ge=1)],
             ):
    return {
        "data": {
            "id": item_id,
            "name": f"Item {item_id}",
        }
    }


@router.post("")
def create_item(
        item: ItemCreate,
        ):
    return {
        "data": {
            "id": 0,
            "name": item.name,
            "description": item.description,
        }
    }