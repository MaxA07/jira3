from models.Users import Users
from fastapi import HTTPException


def users(db):
    try:
        usersList = db.query(Users).all()
        return usersList
    except:
        raise HTTPException(status_code=500)


def addUser(user, position, db):
    try:
        user = Users(name=user, position=position)
        db.add(user)
        db.commit()
        return user
    except:
        raise HTTPException(status_code=500)

