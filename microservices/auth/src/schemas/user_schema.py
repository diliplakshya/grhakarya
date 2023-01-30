"""
    User schema.

    This represents the User schema representing User in database.
"""
from pydantic import BaseModel


class UserBase(BaseModel):
    """
    Base User

    email id is common attribute while creating and reading user and hence creating base class for user.

    Parameters
    ----------
    BaseModel : BaseModel
        Base model used for creating new UserBase model.
    """
    email: str

class UserCreate(UserBase):
    """
    To create user.

    Model used while creating new user in the DB.
    The attributes, like username and password, are received from client are stored in UserCreate model.

    Parameters
    ----------
    UserBase : UserBase
        Base class having email id for the user.
    """
    password: str

class User(UserBase):
    """
    User model.

    Model used while reading user from the DB.
    The attributes, like username and password, retrieved from DB are stored in User model.


    Parameters
    ----------
    UserBase : UserBase
        Base class having details of the user.
    """
    id: int
    is_active: bool

    class Config:
        orm_mode = True
