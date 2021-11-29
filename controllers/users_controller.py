from models.Users import Users
from fastapi import HTTPException


def users(db):
    try:
        usersList = db.query(Users).all()
        return usersList
    except:
        raise HTTPException(status_code=500)


def addUser(user, position,
            email, phone_number, db):
    try:
        user = Users(name=user, position=position,
                     email=email, phone_number=phone_number)
        db.add(user)
        db.commit()
        return user
    except:
        raise HTTPException(status_code=500)


def delete_user_by_id(id, db):
    try:
        record = db.query(Users).get(id)
        db.delete(record)
        db.commit()
        return id
    except:
        raise HTTPException(status_code=404, detail="not found")