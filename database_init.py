from database import engine
from models import Users, Statuses

Users.Base.metadata.create_all(bind=engine)
Statuses.Base.metadata.create_all(bind=engine)