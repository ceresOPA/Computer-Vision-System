
from utils.db import SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends,  HTTPException, APIRouter,Form
from models import User
from pydantic import BaseModel


user_router = APIRouter()


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@user_router.post("/login")
def user_login(username: str, password: str, db: Session = Depends(get_db)):
    print("username",username)
    db_user = User.get_user_byname(db,username)
    if db_user is None:
        return {"msg": "用户名不存在",
                "state": "fail"}
    if db_user.password != password:
        return {"msg": "密码错误",
                "state": "fail"}
    user = {}
    user['id'] = db_user.id
    user['username'] = db_user.username
    user['gender'] = db_user.gender
    user['mark'] = db_user.mark
    user['avatarUrl'] = db_user.avatarUrl
    return user


@user_router.post("/register", response_model=User.BaseUser)
def user_register(username: str, password: str,gender:str ,db: Session = Depends(get_db)):
    db_user = User.add_user(db, username,password,gender)
    return db_user

@user_router.get("/editUser")
def user_edit(username:str,gender:str,id:str ,mark:str,avatarUrl:str,db:Session = Depends(get_db)):
    db_user = User.get_user_byaccount(db,id)
    db_user.username = username
    db_user.gender = gender
    db_user.mark = mark
    db_user.avatarUrl = avatarUrl
    db.commit()
    return {
        "msg":"ok",
        "user":User.get_user_byaccount(db,id)
    }

@user_router.get("/editUserWeb")
def user_edit(username:str,gender:str,id:str ,db:Session = Depends(get_db)):
    db_user = User.get_user_byaccount(db,id)
    db_user.username = username
    db_user.gender = gender
    db.commit()
    return {
        "msg":"ok",
        "user":User.get_user_byaccount(db,id)
    }


@user_router.get("/editPassword")
def user_edit(password:str,id:str ,db:Session = Depends(get_db)):
    db_user = User.get_user_byaccount(db,id)
    db_user.password = password
    db.commit()
    return {
        "msg":"ok",
        "user":User.get_user_byaccount(db,id)
    }

@user_router.get("/checkuser")
def user_check(username:str,db:Session = Depends(get_db)):
    db_user = User.get_user_byname(db,username)
    if db_user is None:
        return {
            "msg": "ok",
            "state": "ok"
        }
    else:
        return {
            "msg": "用户名已存在",
            "state": "fail"
        }

@user_router.get("/test")
def user_test():
    return {"msg": "ok"}
