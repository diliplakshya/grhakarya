"""
    Helper class for hashing.

    This module is responsible for generating hasing for password and creating access token.
"""

from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Union
from ..config.config import settings
from jose import jwt


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    """
    Get hashed password

    To generate hash for the password.

    Parameters
    ----------
    password : str
        Password of the user in plain format.

    Returns
    -------
    str
        Password of the user in hashed format.
    """
    return password_context.hash(password)

def verify_password(password: str, hashed_pass: str) -> bool:
    """
    Verify the provided password.

    The password entered by the user is checked against the hashed version of the same password.

    Parameters
    ----------
    password : str
        Password of the user in plain format.
    hashed_pass : str
        Password of the user in hashed format.

    Returns
    -------
    bool
        True if there is a match else False
    """
    return password_context.verify(password, hashed_pass)

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None) -> str:
    """
    Create access token

    To create access token for a given user using JWT.

    Parameters
    ----------
    data : dict
        User data for which access token to be created.
    expires_delta : Union[timedelta, None]
        Expiry time after which generated access token will be expired.

    Returns
    -------
    str
        Hashed access token using JWT.
    """
    to_encode = data.copy()

    if not expires_delta:
        expires_delta = timedelta(minutes=5)

    expire = datetime.utcnow() + expires_delta

    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
