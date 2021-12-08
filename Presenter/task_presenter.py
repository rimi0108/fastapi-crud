from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import and_
from sqlalchemy.sql.functions import user
from starlette.responses import Response
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from Model import models
from database.schemas import PatchTask, TaskCreate
from database.database import SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_tasks(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Task)
        .filter(models.Task.owner_id == user_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_detail_tasks(
    db: Session, task_id: int, user_id: int, skip: int = 0, limit: int = 100
):
    task = (
        db.query(models.Task)
        .filter(and_(models.Task.owner_id == user_id, models.Task.id == task_id))
        .offset(skip)
        .limit(limit)
        .all()
    )
    if task == []:
        return Response(status_code=HTTP_404_NOT_FOUND)
    return task


def create_user_task(db: Session, task: TaskCreate, user_id: int):
    db_task = models.Task(**task.dict(), owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def modify_task(db: Session, task: PatchTask, user_id: int, task_id: int):

    task.owner_id = user_id
    task.id = task_id

    for key, value in dict(task).items():

        modify_task = (
            db.query(models.Task)
            .filter(and_(models.Task.id == task_id, models.Task.owner_id == user_id))
            .update({key: value})
        )
        db.commit()
        print(key, value)

    return modify_task


def delete_tasks(db: Session, user_id: int):
    task_delete = db.query(models.Task).filter(models.Task.owner_id == user_id)
    if task_delete is None:
        return Response(status_code=HTTP_404_NOT_FOUND, detail="There is no task")
    for i in task_delete:
        db.delete(i)
        db.commit()

    return Response(status_code=HTTP_200_OK)


def delete_one_task(db: Session, task_id: int, user_id: int):
    task_delete = (
        db.query(models.Task)
        .filter(and_(models.Task.id == task_id, models.Task.owner_id == user_id))
        .one()
    )
    if task_delete is None:
        return Response(status_code=HTTP_404_NOT_FOUND, detail="Task not found")
    db.delete(task_delete)
    db.commit()

    return Response(status_code=HTTP_200_OK)

