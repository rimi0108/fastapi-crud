from typing import List

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from Presenter import task_presenter
from Model import models
from database.schemas import PatchTask, Task, TaskCreate
from database.database import SessionLocal, engine
from dependencies import get_current_active_user


models.Base.metadata.create_all(bind=engine)

router = APIRouter(tags=["tasks"], dependencies=[Depends(get_current_active_user)])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create


@router.post("/task", response_model=Task)
async def create_task_for_user(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    user_id = current_user.id
    return task_presenter.create_user_task(db=db, task=task, user_id=user_id)


# Read


@router.get("/task", response_model=List[Task])
async def read_tasks(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    tasks = task_presenter.get_user_tasks(
        db, user_id=current_user.id, skip=skip, limit=limit,
    )
    return tasks


@router.get("/task/{task_id}", response_model=List[Task])
async def read_specific_task(
    task_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    tasks = task_presenter.get_detail_tasks(
        db, user_id=current_user.id, task_id=task_id, skip=skip, limit=limit
    )
    return tasks


# Update


@router.patch("/task/{task_id}", response_model=PatchTask)
async def modify_task(
    task_id: int,
    task: PatchTask,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    tasks = task_presenter.modify_task(
        db, user_id=current_user.id, task=task, task_id=task_id
    )
    return tasks


# Delete


@router.delete("/task")
async def delete_all_tasks(
    db: Session = Depends(get_db), current_user=Depends(get_current_active_user),
):
    task = task_presenter.delete_tasks(db=db, user_id=current_user.id)
    return task


@router.delete("/task/{task_id}")
async def delete_task(
    task_id: int,
    current_user=Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    task = task_presenter.delete_one_task(
        db=db, user_id=current_user.id, task_id=task_id
    )
    return task
