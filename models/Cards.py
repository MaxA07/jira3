
from sqlalchemy import Column, String, ForeignKey
import uuid
import Users, Statuses
from database import Base

class Card(Base):

    __tablename__ = 'cards'
    id = Column(String(), primary_key=True, nullable=False)
    task_name = Column(String())
    description = Column(String())
    user_id = Column(String(), ForeignKey(Users.id)) #возвращать в ответе пару {id юзера и имя юзера}
    status_id = Column(String(), ForeignKey(Statuses.id)) #возвращать в ответе пару {id статуса и имя статуса}

    def __init__(self, task_name=None, description=None,
                 user_id=None, status_id=None):
        self.id = str(uuid.uuid4())
        self.task_name = task_name
        self.description = description
        self.user_id = user_id
        self.status_id = status_id