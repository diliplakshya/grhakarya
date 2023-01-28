from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..schemas.user_schema import UserCreate, User
from ..dependencies.db_dependency import db_session
from ..dao.user_dao import get_user_by_email, create_user


router = APIRouter(
    prefix="/token",
    tags=["token"],
    responses={404: {"description": "Token URL Not found"}},
)

@router.post("/login", response_model=User)
async def create(user: UserCreate, db: Session = Depends(db_session)):
    if get_user_by_email(db=db, email=user.email):
        raise HTTPException(detail="Email Already registered", status_code=status.HTTP_400_BAD_REQUEST)

    return create_user(db=db, user=user)
