from app.db import Base,engine
from app.models import User,Product

def create_db():
    Base.metadata.create_all(engine)