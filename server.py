from database import SessionLocal
from controllers.controller1 import statuses, pushStatus, getStatus
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from models.Statuses import StatusModel

app = FastAPI(debug=True)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/test')
def getTest():
    return jsonable_encoder({'a': '12'})


@app.get('/statuses')
def status(db: Session = Depends(get_db)):
    result = statuses(db)
    return result

@app.post('/statuses')
def postStatus(status: StatusModel, db: Session = Depends(get_db)):
    result = pushStatus(status.name, db)
    return result

#
# @app.get('statuses/{id}')
# def getStatus(id):
#     getStatus(id, db)