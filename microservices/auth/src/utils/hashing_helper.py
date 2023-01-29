from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Union
from ..config.config import settings
from jose import jwt


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()

    if not expires_delta:
        expires_delta = timedelta(minutes=5)

    expire = datetime.utcnow() + expires_delta

    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
