from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"about": "This is a todo api made with fastapi"}


@app.get("/todos")
def get_todos():
    return {"message": "Returns a list of todos"}


@app.get("/todos/{id}")
def get_todo(id: int):
    return {"message": "Returns a todo with the given id"}


@app.post("/todos")
def create_todo():
    return {"message": "Creates a todo with given fields and returns the created todo"}


@app.put("/todos/{id}")
def update_todo(id: int):
    return {"message": "Update a todo with given id and returns the updated todo"}


@app.delete("/todos/{id}")
def delete_todo(id: int):
    return {"message": "Deletes the todo with given id"}
