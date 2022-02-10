from sqlalchemy import Boolean, Column, String
from .base import Base


class Todo(Base):
    __tablename__ = "todos"

    todo = Column(String, nullable=False)
    desc = Column(String, default=None)
    checked = Column(Boolean, server_default='True')
