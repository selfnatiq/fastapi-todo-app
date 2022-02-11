from pydantic import BaseModel
from datetime import datetime

from .user import UserResponse


class TodoBase(BaseModel):
    todo: str
    desc: str | None = None
    checked: bool = False


class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    checked: bool


class TodoResponse(TodoBase):
    id: str
    desc: str
    user: UserResponse
    updated_at: datetime
    created_at: datetime

    class Config:
        orm_mode = True
