from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import Session


Base = declarative_base()


class Statuses(Base):
    __tablename__ = 'statuses'
    id = Column(String(), primary_key=True)
    name = Column(String())

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(String(), primary_key=True)


connect = create_engine('postgresql://postgres:nomad_43@localhost:5432/testdb', echo=True)



session = Session(connect)
session.add(Task(id=None))
session.commit()
session.close()
