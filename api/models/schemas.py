from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class SandwichBase(BaseModel):
    sandwich_name: str
    price: float
    calories: int


class SandwichCreate(SandwichBase):
    pass


class SandwichUpdate(BaseModel):
    sandwich_name: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None


class Sandwich(SandwichBase):
    id: int

    class ConfigDict:
        from_attributes = True


class OrderDetailBase(BaseModel):
    amount: int


class OrderDetailCreate(OrderDetailBase):
    order_id: int
    sandwich_id: int

class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    sandwich_id: Optional[int] = None
    amount: Optional[int] = None
    status: Optional[str] = None


class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    sandwich: Optional[Sandwich] = None
    delivery: bool
    tracking_number: int
    status: str

    class ConfigDict:
        from_attributes = True


class OrderBase(BaseModel):
    customer_name: str


class OrderCreate(OrderBase):
    address: str
    description: Optional[str] = None


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None
    address: Optional[str] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True


class PaymentBase(BaseModel):
    price: int


class PaymentCreate(PaymentBase):
    order_id: int
    cash: bool
    promo_id: str


class PaymentUpdate(BaseModel):
    price: Optional[int] = None
    order_id: Optional[int] = None
    cash: Optional[bool] = None
    promo_id: Optional[str] = None


class Payment(PaymentBase):
    id: int

    class ConfigDict:
        from_attributes = True


class PromoBase(BaseModel):
    promo_id: str


class PromoCreate(PromoBase):
    discount: int
    expiration: datetime


class PromoUpdate(PromoBase):
    discount: Optional[int] = None
    expiration: Optional[datetime] = None
    promo_id: Optional[str] = None


class Promo(BaseModel):
    id: int

    class ConfigDict:
        from_attributes = True


class ResourceBase(BaseModel):
    item: str
    amount: int


class ResourceCreate(ResourceBase):
    pass


class ResourceUpdate(BaseModel):
    item: Optional[str] = None
    amount: Optional[int] = None


class Resource(ResourceBase):
    id: int

    class ConfigDict:
        from_attributes = True


class RecipeBase(BaseModel):
    amount: int


class RecipeCreate(RecipeBase):
    sandwich_id: int
    resource_id: int

class RecipeUpdate(BaseModel):
    sandwich_id: Optional[int] = None
    resource_id: Optional[int] = None
    amount: Optional[int] = None

class Recipe(RecipeBase):
    id: int
    sandwich: Sandwich
    resource: Resource

    class ConfigDict:
        from_attributes = True


class ReviewBase(BaseModel):
    comment: str
    rating: int

class ReviewCreate(ReviewBase):
    order_id: int

class ReviewUpdate(BaseModel):
    order_id: Optional[int] = None
    comment: Optional[str] = None
    rating: Optional[int] = None


class Review(ReviewBase):
    id: int

    class ConfigDict:
        from_attributes = True


class CustomerBase(BaseModel):
    customer_name: str


class CustomerCreate(OrderBase):
    email: str
    phone: int
    address: str


class CustomerUpdate(BaseModel):
    customer_name: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[int] = None


class Customer(OrderBase):
    id: int

    class ConfigDict:
        from_attributes = True
