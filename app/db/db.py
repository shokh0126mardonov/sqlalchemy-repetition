from sqlalchemy import (
    create_engine,
    URL,
    )
from sqlalchemy.orm import declarative_base,sessionmaker

from app.db.config import settings


url_object = URL.create(
    drivername="postgresql+psycopg2",
    username=settings.DB_USER,
    password=settings.DB_PASS,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.DB_NAME
)

engine = create_engine(url_object)

Base = declarative_base()

LocalSession = sessionmaker(bind=engine)