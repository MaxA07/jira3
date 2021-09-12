from models.Statuses import Statuses
from fastapi import HTTPException


def statuses(db):
    try:
        a = db.query(Statuses).all()
        return a
    except:
        raise HTTPException(status_code=500)


def pushStatus(status, db):
    status = Statuses(name=status)
    db.add(status)
    db.commit()
    return status


def getStatus(id, db):
    try:
        return str(id)
    except:
        HTTPException(status_code=400, detail="not found")
