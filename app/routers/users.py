
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..schemas import user as user_schema
from ..controllers import users as users_controller
from ..core import deps

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=user_schema.UserResponse)
def create_user(user: user_schema.UserCreate, db: Session = Depends(deps.get_db)):
    db_user = users_controller.get_user(db, user.username)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="The user with this username already exists in the system.")

    db_user = users_controller.create_user(db, user)
    return db_user
