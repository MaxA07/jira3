from sqlalchemy import Column, String
import uuid
from database import Base
from pydantic import BaseModel


class StatusModel(BaseModel):
    name: str


class Statuses(Base):
    __tablename__ = 'statuses'
    id = Column(String(), primary_key=True)
    name = Column(String())

    def __init__(self, name=None):
        self.id = str(uuid.uuid4())
        self.name = name

