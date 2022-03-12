from database import engine, Base
from models import Users, Statuses

Base.metadata.create_all(bind=engine)
