from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    price = Column(DECIMAL(4, 2), nullable=False, server_default='0.0')
    cash = Column(Boolean, index=True, nullable=False)
    code = Column(String, nullable=False)

    order = relationship("Order", back_populates="payments")
    promo = relationship("Promo", back_populates="payments")
