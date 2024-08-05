from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
    amount = Column(Integer, index=True, nullable=False)
    delivery = Column(Boolean, index=True, nullable=False)

    sandwich = relationship("Sandwich", back_populates="order_details")
    order = relationship("Order", back_populates="order_details")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    address = Column(String(300))
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    description = Column(String(300))

    order_details = relationship("OrderDetail", back_populates="order")
    payments = relationship("Payment", back_populates="order")
    reviews = relationship("Review", back_populates="order")


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    price = Column(DECIMAL(4, 2), nullable=False, server_default='0.0')
    cash = Column(Boolean, index=True, nullable=False)
    code = Column(String, nullable=False)

    order = relationship("Order", back_populates="payments")
    promo = relationship("Promo", back_populates="payments")


class Promo(Base):
    __tablename__ = "promos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    expiration = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    code = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)

    payment = relationship("Payment", back_populates="promo")


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
    resource_id = Column(Integer, ForeignKey("resources.id"))
    amount = Column(Integer, index=True, nullable=False, server_default='0.0')
    time = Column(Integer, index=True, nullable=False, server_default='5')

    sandwich = relationship("Sandwich", back_populates="recipes")
    resource = relationship("Resource", back_populates="recipes")


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item = Column(String(100), unique=True, nullable=False)
    amount = Column(Integer, index=True, nullable=False, server_default='0.0')

    recipes = relationship("Recipe", back_populates="resource")


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    review = Column(String(300))
    rating = Column(Integer, index=True, nullable=False, server_default='0')

    orders = relationship("Order", back_populates="reviews")


class Sandwich(Base):
    __tablename__ = "sandwiches"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sandwich_name = Column(String(100), unique=True, nullable=True)
    price = Column(DECIMAL(4, 2), nullable=False, server_default='0.0')

    recipes = relationship("Recipe", back_populates="sandwich")
    order_details = relationship("OrderDetail", back_populates="sandwich")