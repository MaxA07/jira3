from sqlalchemy import Column, String
import uuid
from database import Base


class Users(Base):
    __tablename__ = 'users'
    id = Column(String(), primary_key=True, nullable=False)
    name = Column(String())
    position = Column(String())
    email = Column(String())
    phone_number = Column(String())

    def __init__(self, name=None, position=None,
                 email=None, phone_number=None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.position = position
        self.email = email
        self.phone_number = phone_number

