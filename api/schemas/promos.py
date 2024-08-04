from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .resources import Resource
from .sandwiches import Sandwich


class PromoBase(BaseModel):
    id: int


class PromoCreate(PromoBase):
    amount: int
    expiration: datetime
    code: str


class PromoUpdate(PromoBase):
    id: int
    amount: int
    expiration: datetime
    code: str


class Promo(BaseModel):
    id: int
    amount: int
    expiration: datetime
    code: str

    class ConfigDict:
        from_attributes = True