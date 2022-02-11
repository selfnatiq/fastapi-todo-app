from pydantic import BaseModel
from .user import UserResponse


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    username: str


class TokenResponse(BaseModel):
    jwt: str
    user: UserResponse
