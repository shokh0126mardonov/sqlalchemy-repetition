from sqlalchemy import Column,Integer,String,DECIMAL

from ..db import Base


class ProductModel(Base):
    __tablename__ = 'products'

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(length=128),nullable=False,unique=True)
    price = Column(DECIMAL(),nullable=False)
    quantity = Column(Integer,nullable=False)