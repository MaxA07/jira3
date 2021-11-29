from database import SessionLocal
from controllers.status_controller import statuses, pushStatus, delete_status_by_id
from controllers.users_controller import users, addUser, delete_user_by_id
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from cruds.StatusCrud import GetStatusModel
from cruds.User_Cruds import GetUserModel


app = FastAPI(debug=True)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/statuses')
def status(db: Session = Depends(get_db)):
    result = statuses(db)
    return result


@app.post('/statuses')
def post_status(status: GetStatusModel, db: Session = Depends(get_db)):
    result = pushStatus(status.name, db)
    return result


@app.delete('/statuses/', include_in_schema=False)
def delete_status(id, db: Session = Depends(get_db)):
    result = delete_status_by_id(id, db)
    return result


@app.get('/users')
def get_data(db: Session = Depends(get_db)):
    result = users(db)
    return result


@app.post('/users')
def post_user(user: GetUserModel, db: Session = Depends(get_db)):
    result = addUser(user.name, user.position,
                     user.email, user.phone_number, db)
    return result


@app.delete('/users/', include_in_schema=False)
def delete_user(id, db: Session = Depends(get_db)):
    result = delete_user_by_id(id, db)
    return result