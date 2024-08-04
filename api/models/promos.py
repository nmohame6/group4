from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Promo(Base):
    __tablename__ = "promos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    expiration = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    code = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)

    payment = relationship("Payment", back_populates="promo")