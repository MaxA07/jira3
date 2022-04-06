from cruds.StatusCrud import CreateStatusModel, UpdateStatusModel
from database import get_db
from models.Statuses import Statuses
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

status_route = APIRouter(
    prefix="/status"
)

@status_route.get('')
def status(db: Session = Depends(get_db)):
    try:
        return db.query(Statuses).all()
    except:
        raise HTTPException(status_code=500)


@status_route.post('')
def post_status(status: CreateStatusModel, db: Session = Depends(get_db)):
    try:
        status = Statuses(name=status)
        db.add(status)
        db.commit()
        return status
    except:
        raise HTTPException(status_code=500)


@status_route.put('')
def post_status(status: UpdateStatusModel, db: Session = Depends(get_db)):
    try:
        db_status = db.query(Statuses).filter(Statuses.id == status.id).one_or_none()
        if db_status is None:
            return HTTPException(status_code=404)

        update_data = status.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_status, key, value)
        db.commit()

        return status
    except:
            raise HTTPException(status_code=500)

@status_route.delete('/')
def delete_status(ids: str, db: Session = Depends(get_db)):
    try:
        ids_list = ids.split(',')
        for id in ids_list:
            record = db.query(Statuses).get(id)
            db.delete(record)
        db.commit()
        return ids
    except:
        raise HTTPException(status_code=404, detail="not found")

