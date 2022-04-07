from models.Card import Card
from fastapi import HTTPException

def cards(db):
    try:
        usersList = db.query(Card).all()
        return usersList
    except:
        raise HTTPException(status_code=500)