from fastapi import APIRouter
from pydantic import BaseModel
from ..dao import Dao
from typing import Union


router = APIRouter(
    prefix="/milk",
    tags=["milk"],
    responses={404: {"description": "Not found"}},
)

class Milk(BaseModel):
    uid: str
    quantity: int
    price: int = None
    description: Union[str, None] = None


@router.post("/")
async def create(milk: Milk):
    dao = Dao()
    return dao.create(milk.dict())

@router.get("/")
async def get(uid: str):
    dao = Dao()
    return dao.get(uid)