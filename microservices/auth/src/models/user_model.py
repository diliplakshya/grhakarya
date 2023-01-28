from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..db.connection import Base


class User(Base):
    """
    User Model

    To create table in DB for user.

    Parameters
    ----------
    Base : _type_
        _description_
    """
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(30), unique=True, index=True)
    hashed_password = Column(String(60))
    is_active = Column(Boolean, default=True)
