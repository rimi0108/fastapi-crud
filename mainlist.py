from fastapi import responses
import requests

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


app = FastAPI()

db = []

# ---------------------------------------------------------------------------------------
# dats: models
# ---------------------------------------------------------------------------------------


class ToDoList(BaseModel):
    name: str
    completed: bool


class ToDoListModify(BaseModel):
    id: int
    name: str
    completed: bool


templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
    return {"Hello": "World!"}


@app.get("/todolists", response_class=HTMLResponse)
def get_todolists(request: Request):
    context = {}

    rsToDoList = []

    cnt = 0

    for todolist in db:
        cnt += 1
        rsToDoList.append(
            {"id": cnt, "name": todolist["name"], "completed": todolist["completed"],}
        )

    context["request"] = request
    context["rsToDoList"] = rsToDoList

    return templates.TemplateResponse("todolist.html", context)


@app.get("/todolists/{todolist_id}")
def get_todolist(request: Request, todolist_id: int):
    todolist = db[todolist_id - 1]

    context =  { "request": request, "name": todolist["name"], "completed": todolist["completed"] }

    return templates.TemplateResponse("todolist_detail.html", context)


@app.post("/todolists")
def create_todolist(todolist: ToDoList):
    db.append(todolist.dict())

    return db[-1]


@app.put("/todolists")
def modify_todolist(todolist: ToDoListModify):
    db[todolist.id - 1] = {"name": todolist.name, "completed": todolist.completed}

    return db[todolist.id - 1]


@app.delete("/todolists/{todolist_id}")
def delete_todolist(todolist_id: int):
    db.pop(todolist_id - 1)

    return db
