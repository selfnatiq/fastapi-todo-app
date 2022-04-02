from sqlalchemy import asc
from sqlalchemy.orm import Session

from ..models import todo as todo_model, user as user_model
from ..schemas import todo as todo_schema


def get_todo(db: Session, todo_id: str):
    return db.query(todo_model.Todo).filter(todo_model.Todo.id == todo_id).first()


def get_todos(db: Session, skip: int = 0, limit: int = 20):
    return db \
        .query(todo_model.Todo) \
        .order_by(asc(todo_model.Todo.created_at)) \
        .offset(skip).limit(limit).all()


def create_todo(db: Session, todo: todo_schema.TodoCreate, user: user_model.User):
    db_todo = todo_model.Todo(**todo.dict(), user=user)
    db.add(db_todo)

    db.commit()
    db.refresh(db_todo)

    return db_todo


def update_todo(db: Session, todo_id: str, todo: todo_schema.TodoUpdate):
    db_todo_query = db.query(todo_model.Todo).filter(todo_model.Todo.id == todo_id)
    db_todo = db_todo_query.first()

    if db_todo is None:
        return None

    db_todo_query.update(todo.dict(), synchronize_session=False)
    db.commit()

    return db_todo


def delete_todo(db: Session, todo_id: str):
    db_todo_query = db.query(todo_model.Todo).filter(todo_model.Todo.id == todo_id)
    db_todo = db_todo_query.first()

    if db_todo is None:
        return None

    db_todo_query.delete(synchronize_session=False)
    db.commit()

    return 201
