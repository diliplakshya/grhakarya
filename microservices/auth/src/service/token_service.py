from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from ..dao.user_dao import get_user_by_email, create_user
from ..utils.hashing_helper import get_hashed_password, verify_password, create_access_token
from ..dependencies.oauth_dependency import oauth2_scheme
from ..config.config import settings
from ..schemas.user_schema import User, UserCreate
from ..schemas.token_schema import Token, TokenData


credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

def generate_access_token(username: str):
    return create_access_token(
        data={"sub": username}, expires_delta=timedelta(minutes=settings.access_token_expire_minutes)
    )

def create_new_user(db: Session, user: UserCreate):
    if get_user_by_email(db=db, email=user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Duplicate user.",
        )
        
    user.password = get_hashed_password(user.password)
    return create_user(db=db, user=user)


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db=db, email=email)
    return False if not user or not verify_password(password, get_hashed_password(password)) else user

async def decode_token(token: str = Depends(oauth2_scheme)):
    username = None

    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        username: str = payload.get("sub")
    except JWTError:
        raise credentials_exception

    return username

async def get_current_user():
    username = None

    try:
        username: str = decode_token()
    except Exception as exp:
        raise exp

    user = get_user_by_email(email=username)

    if user is None:
        raise credentials_exception
        
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")

    return current_user