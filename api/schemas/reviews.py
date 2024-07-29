from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from sqlalchemy.util import string_or_unprintable
from .orders import Order


class ReviewBase(BaseModel):
    review: str
    rating: int

class ReviewCreate(ReviewBase):
    order_id: int

class ReviewUpdate(BaseModel):
    order_id: Optional[int] = None
    review: Optional[str] = None
    rating: Optional[int] = None

class Review(ReviewBase):
    id: int

    class ConfigDict:
        from_attributes = True
        