from pydantic import BaseModel
from sqlalchemy.orm import Session
from utils import db as DataBase
import random


class BaseUser(BaseModel):
    username: str
    password: str
    gender: str
    mark: str
    avatarUrl :str

    class Config:
        orm_mode = True


def add_user(db: Session, username:str,password:str,gender:str):
    db_user = DataBase.User(username=username, password=password,gender=gender,mark='',avatarUrl=f'/assets/avatar{random.randint(0,11)}.png')
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_byname(db: Session, user_id: str):
    return db.query(DataBase.User).filter(DataBase.User.username == user_id).first()


def get_user_byaccount(db: Session, user_id: str):
    return db.query(DataBase.User).filter(DataBase.User.id == user_id).first()

