from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    username: str
    password: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserResponse(BaseModel):
    id: str
    username: str
    updated_at: datetime
    created_at: datetime

    class Config:
        orm_mode = True
