from controllers.status_controller import status_route
from database import SessionLocal, get_db
# from controllers.status_controller import statuses, push_status, delete_statuses_by_id
from controllers.users_controller import users, addUser, delete_user_by_id
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from cruds.User_Cruds import GetUserModel


app = FastAPI(debug=True)
app.include_router(status_route)


@app.get('/')
def root():
    return "status active"


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
def delete_user(ids, db: Session = Depends(get_db)):
    result = delete_user_by_id(ids, db)
    return result
