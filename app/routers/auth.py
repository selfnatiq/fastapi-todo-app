
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..schemas import auth
from ..controllers import users as users_controller
from ..core import security, deps

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("", response_model=auth.TokenResponse)
def login(user_data: OAuth2PasswordRequestForm = Depends(),
          db: Session = Depends(deps.get_db)):
    user = users_controller.authenticate(db, user_data.username, user_data.password)

    if not user:
        raise HTTPException(status=status.HTTP_400_BAD_REQUEST,
                            detail="Invalid username or password")

    access_token = security.create_access_token({"username": user.username})
    return {"jwt": access_token, "user": user}
