from sqlalchemy.orm import Session

from ..models import user as user_model
from ..schemas import user as user_schema
from ..core import security


def get_user(db: Session, username: str):
    return db.query(user_model.User).filter(user_model.User.username == username).first()


def create_user(db: Session, user: user_schema.UserCreate):
    password_hash = security.get_password_hash(user.password)
    db_user = user_model.User(**user.dict())
    db_user.password = password_hash

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def authenticate(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user or not security.verify_password(password, user.password):
        return None

    return user
