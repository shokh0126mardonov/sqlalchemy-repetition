from sqlalchemy import Column, Integer, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from ..db import Base

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)

    total_price = Column(DECIMAL(10, 2), nullable=False)

    user = relationship("User", back_populates="orders")
