"""
    Token schema.

    This represents the Token schema representing Access token for the user.
"""
from pydantic import BaseModel
from typing import Union


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None
