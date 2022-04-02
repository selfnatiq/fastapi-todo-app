from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..schemas import todo as todo_schema
from ..controllers import todos as todos_controller
from .. import utils
from ..core import deps
from ..models import user

router = APIRouter(prefix="/todos", tags=["Todos"])


@router.get("/", response_model=list[todo_schema.TodoResponse])
def read_todos(
        skip: int = 0,
        limit: int = 20,
        db: Session = Depends(deps.get_db),
        current_user: user.User = Depends(deps.get_current_user)):
    db_todos = todos_controller.get_todos(db, skip, limit)
    return db_todos


@router.get("/{id}", response_model=todo_schema.TodoResponse)
def read_todo(id: str, db: Session = Depends(deps.get_db)):
    todo = todos_controller.get_todo(db, id)
    if todo is None:
        utils.raise_not_found_exception()

    return todo


@router.post("/", response_model=todo_schema.TodoResponse)
def create_todo(
        todo: todo_schema.TodoCreate,
        db: Session = Depends(deps.get_db),
        current_user: user.User = Depends(deps.get_current_user)):
    created_todo = todos_controller.create_todo(db, todo, current_user)
    return created_todo


@router.put("/{id}", response_model=todo_schema.TodoResponse)
def update_todo(id: str, todo: todo_schema.TodoUpdate, db: Session = Depends(deps.get_db)):
    updated_todo = todos_controller.update_todo(db, id, todo)
    if updated_todo is None:
        utils.raise_not_found_exception()

    return updated_todo


@router.delete("/{id}")
def delete_todo(id: str, db: Session = Depends(deps.get_db)):
    deleted_todo = todos_controller.delete_todo(db, id)
    if deleted_todo is None:
        utils.raise_not_found_exception()

    return deleted_todo
