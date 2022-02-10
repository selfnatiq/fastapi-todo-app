from sqlalchemy import Column, String
from .base import Base


class User(Base):
    __tablename__ = "users"

    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
