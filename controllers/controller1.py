from models.Statuses import Statuses
from fastapi import HTTPException


def statuses(db):
    try:
        statusList = db.query(Statuses).all()
        return statusList
    except:
        raise HTTPException(status_code=500)


def pushStatus(status, db):
    try:
        status = Statuses(name=status)
        db.add(status)
        db.commit()
        return status
    except:
        raise HTTPException(status_code=500)


def delete_status_by_id(id, db):
    try:
        record = db.query(Statuses).get(id)
        db.delete(record)
        db.commit()
        return id
    except:
        raise HTTPException(status_code=404, detail="not found")
