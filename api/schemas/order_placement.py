from pydantic import BaseModel, Field
from typing import Optional

class OrderDetailCreate(BaseModel):
    order_id: int = 
    sandwich_id: int = 
    amount: int = Field