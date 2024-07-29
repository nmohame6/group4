from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .orders import Order



class PaymentBase(BaseModel):
  id: int
  price: int

class PaymentCreate(PaymentBase):
  order_id: int

class PaymentUpdate(BaseModel):
  id: Optional[int] = None
  price: Optional[int] = None
  order_id: Optional[int] = None

class Payment(PaymentBase):
  cash: bool

  class ConfigDict:
    from_attributes = True
