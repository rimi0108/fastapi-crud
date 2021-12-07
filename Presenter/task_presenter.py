from sqlalchemy.orm import Session
from starlette.responses import Response
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from Model import models
from database.schemas import TaskCreate
from database.database import SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()


def create_user_task(db: Session, task: TaskCreate, user_id: int):
    db_task = models.Task(**task.dict(), owner_id=user_id)
    print(db_task)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def modify_task(db: Session, task: TaskCreate, task_id: int):
    task_update = db.query(models.Task).filter_by(task_id=task_id)
    if task_update is None:
        return Response(status_code=HTTP_404_NOT_FOUND, detail="Task not found")
    db_task = models.Task(**task.dict(),)


def delete_tasks(db: Session):
    task_delete = db.query(models.Task).all()
    if task_delete is None:
        return Response(status_code=HTTP_404_NOT_FOUND, detail="There is no task")
    for i in task_delete:
        db.delete(i)
        db.commit()

    return Response(status_code=HTTP_200_OK)


def delete_one_task(db: Session, task_id: int):
    task_delete = db.query(models.Task).filter(models.Task.id == task_id).one()
    if task_delete is None:
        return Response(status_code=HTTP_404_NOT_FOUND, detail="Task not found")
    db.delete(task_delete)
    db.commit()

    return Response(status_code=HTTP_200_OK)

