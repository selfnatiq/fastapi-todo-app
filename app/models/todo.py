from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship

from .base import Base


class Todo(Base):
    __tablename__ = "todos"

    todo = Column(String, nullable=False)
    desc = Column(String, default=None)
    checked = Column(Boolean, server_default='True')
    user_id = Column(postgresql.UUID, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User", back_populates="todos")
