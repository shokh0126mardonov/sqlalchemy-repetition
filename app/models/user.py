from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship

from ..db import Base

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True,nullable=False)
    password = Column(String(length=64))
    first_name = Column(String)
    last_name = Column(String)

    orders = relationship(
        "Order",
        back_populates="user",
        cascade="all, delete-orphan"
    )