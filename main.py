import requests

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

db = []


class ToDoList(BaseModel):
    name: str
    completed: bool


# @app.get("/")
# def root():
#     return {"Hello": "World!"}


@app.get("/todolists")
def get_todolists():
    results = []
    for todolist in db:
        results.append(
            {"name": todolist["name"], "completed": todolist["completed"],}
        )

    return results


@app.get("/todolists/{todolist_id}")
def get_todolist(todolist_id: int):
    todolist = db[todolist_id - 1]
    return {"name": todolist["name"], "completed": todolist["completed"]}


@app.post("/todolists")
def create_todolist(todolist: ToDoList):
    db.append(todolist.dict())

    return db[-1]


@app.delete("/todolists/{todolist_id}")
def delete_todolist(todolist_id: int):
    db.pop(todolist_id - 1)

    return db
