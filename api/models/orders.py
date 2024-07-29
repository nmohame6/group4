from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    address = Column(String(300))
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    description = Column(String(300))

    order_details = relationship("OrderDetail", back_populates="order")
    payments = relationship("Payment", back_populate="order")
    reviews = relationship("Review", back_populate="order")
