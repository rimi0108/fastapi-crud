from typing import List, Optional

from pydantic import BaseModel

from database.database import Base


class TaskBase(BaseModel):
    name: str
    completed: bool


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class PatchTask(TaskBase):
    id: Optional[int]
    owner_id: Optional[int]
    name: Optional[str]
    completed: Optional[bool]

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserInDB(UserBase):
    hashed_password: str


class User(UserBase):
    id: int
    is_active: bool
    tasks: List[Task] = []

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None

