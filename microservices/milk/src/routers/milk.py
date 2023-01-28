from fastapi import APIRouter
from pydantic import BaseModel
from typing import Union


router = APIRouter(
    prefix="/milk",
    tags=["milk"],
    responses={404: {"description": "Milk URL Not found"}},
)

class Milk(BaseModel):
    uid: str
    quantity: int
    price: int = None
    description: Union[str, None] = None

@router.get("/")
async def get(milk: Milk):
    return "Milk"
    

