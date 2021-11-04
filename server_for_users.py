from database import SessionLocal
from controllers.users_controller import users, addUser, delete_user_by_id
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from cruds.User_Cruds import GetUserModel

app = FastAPI(debug=True)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/users')
def name(db: Session = Depends(get_db)):
    result = users(db)
    return result


@app.post('/users')
def add_name(status: GetUserModel, db: Session = Depends(get_db)):
    result = addUser(users.name, db)
    return result