from fastapi import APIRouter, Depends
from pydantic import BaseModel
from ..dao import Dao
from typing import Union
from ..security import get_current_active_user, User


router = APIRouter(
    prefix="/milk",
    tags=["milk"],
    # dependencies=[Depends(get_current_active_user)],
    responses={404: {"description": "Milk URL Not found"}},
)

class Milk(BaseModel):
    uid: str
    quantity: int
    price: int = None
    description: Union[str, None] = None

@router.post("/", response_model=User)
async def create(milk: Milk, current_user: User = Depends(get_current_active_user)):
    dao = Dao()
    return dao.create(milk.dict())
    
@router.get("/", response_model=User)
async def get(uid: str, current_user: User = Depends(get_current_active_user)):
    dao = Dao()
    return dao.get(uid)
