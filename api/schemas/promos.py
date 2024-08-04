from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .resources import Resource
from .sandwiches import Sandwich


class PromoBase(BaseModel):
    discount: int


class PromoCreate(PromoBase):
    

class Promo(BaseModel):
    amount: Optional[int] = None
    discount : int
    discountedamount: amount - (amount*discount)
    
class Promo(PromoBase):
    discount : Discount
    amount : Amount

    class ConfigDict:
        from_attributes = True