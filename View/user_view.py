from typing import List

from fastapi import Depends, HTTPException, APIRouter
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from starlette.responses import Response
from starlette.status import HTTP_404_NOT_FOUND

from Model.models import Base
from Presenter import user_presenter
from Presenter.user_presenter import get_user
from database.schemas import User, UserCreate, Token
from database.database import SessionLocal, engine
from dependencies import *

Base.metadata.create_all(bind=engine)

router = APIRouter(tags=["users"],)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/user", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = user_presenter.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_presenter.create_user(db=db, user=user)


@router.get("/users", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_presenter.get_user(db, skip=skip, limit=limit)
    return users


def fake_hash_password(password: str):
    return "fakehashed" + password


@router.post("/token", response_model=Token)
async def get_access_token(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id=user_id)
    if user is None:
        return Response(status_code=HTTP_404_NOT_FOUND)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(
        data={"sub": user_id}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
