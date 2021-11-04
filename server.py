from database import SessionLocal
from controllers.status_controller import statuses, pushStatus, delete_status_by_id
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from cruds.StatusCrud import GetStatusModel

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

