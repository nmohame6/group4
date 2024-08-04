from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    review = Column(String(300))
    rating = Column(Integer, index=True, nullable=False, server_default='0')

    orders = relationship("Order", back_populates="reviews")
    