from fastapi import Depends
from sqlalchemy.orm import Session
from ..models import user_model
from ..schemas import user_schema
from ..dependencies.db_dependency import db_session
from ..utils.hashing_helper import get_hashed_password

def get_user(user_id: int, db: Session = Depends(db_session)):
    return db.query(user_model.User).filter(user_model.User.id == user_id).first()

def get_user_by_email(email: str, db: Session = Depends(db_session)):
    return db.query(user_model.User).filter(user_model.User.email == email).first()

def create_user(user: user_schema.UserCreate, db: Session = Depends(db_session)):
    db_user = user_model.User(email=user.email, hashed_password=get_hashed_password(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
