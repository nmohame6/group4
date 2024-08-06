from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .models import models, schemas
from .controllers import orders, reviews, promos
from .controllers import sandwiches
from .controllers import recipes
from .controllers import resources
from .controllers import order_details
from .controllers import payments
from .dependencies.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


## endpoints for orders
@app.post("/orders/", response_model=schemas.Order, tags=["Orders"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, order=order)


@app.get("/orders/", response_model=list[schemas.Order], tags=["Orders"])
def read_orders(db: Session = Depends(get_db)):
    return orders.read_all(db)


@app.get("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order


@app.put("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def update_one_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_db = orders.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.update(db=db, order=order, order_id=order_id)


@app.delete("/orders/{order_id}", tags=["Orders"])
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.delete(db=db, order_id=order_id)


##endpoints for sandwiches
@app.post("/sandwiches/", response_model=schemas.Sandwich, tags=["Sandwiches"])
def create_sandwich(sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    return sandwiches.create(db=db, sandwich=sandwich)


@app.get("/sandwiches/", response_model=list[schemas.Sandwich], tags=["Sandwiches"])
def read_sandwiches(db: Session = Depends(get_db)):
    return sandwiches.read_all(db)


@app.get("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
def read_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = sandwiches.read_one(db, sandwich_id=sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return sandwich


@app.put("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
def update_one_sandwich(sandwich_id: int, sandwich: schemas.SandwichUpdate, db: Session = Depends(get_db)):
    sandwich_db = sandwiches.read_one(db, sandwich_id=sandwich_id)
    if sandwich_db is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return sandwiches.update(db=db, sandwich=sandwich, sandwich_id=sandwich_id)


@app.delete("/sandwiches/{sandwich_id}", tags=["Sandwiches"])
def delete_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = sandwiches.read_one(db, sandwich_id=sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return sandwiches.delete(db=db, sandwich_id=sandwich_id)


# endpoints for recipes
@app.post("/recipes/", response_model=schemas.Recipe, tags=["Recipes"])
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return recipes.create(db=db, request=recipe)


@app.get("/recipes/", response_model=list[schemas.Recipe], tags=["Recipes"])
def read_recipes(db: Session = Depends(get_db)):
    return recipes.read_all(db)


@app.get("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["Recipes"])
def read_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = recipes.read_one(db, recipe_id=recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe


@app.put("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["Recipes"])
def update_one_recipe(recipe_id: int, recipe: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    recipe_db = recipes.read_one(db, recipe_id=recipe_id)
    if recipe_db is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipes.update(db=db, recipe=recipe, recipe_id=recipe_id)


@app.delete("/recipes/{recipe_id}", tags=["Recipes"])
def delete_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = recipes.read_one(db, recipe_id=recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipes.delete(db=db, recipe_id=recipe_id)


# endpoints for resources
@app.post("/resources/", response_model=schemas.Resource, tags=["Resources"])
def create_resource(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return resources.create(db=db, resource=resource)


@app.get("/resources/", response_model=list[schemas.Resource], tags=["Resources"])
def read_resources(db: Session = Depends(get_db)):
    return resources.read_all(db)


@app.get("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def read_one_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = resources.read_one(db, resource_id=resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource


@app.put("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def update_one_resource(resource_id: int, resource: schemas.ResourceUpdate, db: Session = Depends(get_db)):
    resource_db = resources.read_one(db, resource_id=resource_id)
    if resource_db is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resources.update(db=db, resource=resource, resource_id=resource_id)


@app.delete("/resources/{resource_id}", tags=["Resources"])
def delete_one_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = resources.read_one(db, resource_id=resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resources.delete(db=db, resource_id=resource_id)


# endpoints for order details
@app.post("/order_details/", response_model=schemas.OrderDetail, tags=["Order_details"])
def create_order_detail(OrderDetail: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    return order_details.create(db=db, request=OrderDetail)


@app.get("/order_details/", response_model=list[schemas.OrderDetail], tags=["Order_details"])
def read_order_details(db: Session = Depends(get_db)):
    return order_details.read_all(db)


@app.get("/order_details/{OrderDetail_id}", response_model=schemas.OrderDetail, tags=["Order_details"])
def read_one_order_detail(OrderDetail_id: int, db: Session = Depends(get_db)):
    OrderDetail = order_details.read_one(db, item_id=OrderDetail_id)
    if OrderDetail is None:
        raise HTTPException(status_code=404, detail="Order detail not found")
    return OrderDetail


@app.put("/order_details/{OrderDetail_id}", response_model=schemas.OrderDetail, tags=["Order_details"])
def update_one_order_detail(OrderDetail_id: int, OrderDetail: schemas.OrderDetailUpdate, db: Session = Depends(get_db)):
    OrderDetail_db = order_details.read_one(db, item_id=OrderDetail_id)
    if OrderDetail_db is None:
        raise HTTPException(status_code=404, detail="Order detail not found")
    return order_details.update(db=db, request=OrderDetail, item_id=OrderDetail_id)


@app.delete("/order_details/{OrderDetail_id}", tags=["Order_details"])
def delete_one_order_detail(OrderDetail_id: int, db: Session = Depends(get_db)):
    OrderDetail = order_details.read_one(db, item_id=OrderDetail_id)
    if OrderDetail is None:
        raise HTTPException(status_code=404, detail="Order detail not found")
    return order_details.delete(db=db, item_id=OrderDetail_id)

##endpoints for payments
@app.post("/payments/", response_model=schemas.Payment, tags=["Payments"])
def create_payment(payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
    return payments.create(db=db, request=payment)


@app.get("/payments/", response_model=list[schemas.Payment], tags=["Payments"])
def read_payments(db: Session = Depends(get_db)):
    return payments.read_all(db)


@app.get("/payments/{Payments_id}", response_model=schemas.Payment, tags=["Payments"])
def read_one_payment(Payment_id: int, db: Session = Depends(get_db)):
    Payment = payments.read_one(db, item_id=Payment_id)
    if Payment is None:
        raise HTTPException(status_code=404, detail="Order detail not found")
    return Payment


@app.put("/payments/{Payments_id}", response_model=schemas.Payment, tags=["Payments"])
def update_one_payment(Payment_id: int, Payment: schemas.PaymentUpdate, db: Session = Depends(get_db)):
    Payment_db = payments.read_one(db, item_id=Payment_id)
    if Payment_db is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payments.update(db=db, request=Payment, item_id=Payment_id)


@app.delete("/payments/{payment_id}", tags=["Payments"])
def delete_one_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = payments.read_one(db, item_id=payment_id)
    if payment is None:
        raise HTTPException(status_code=404, detail="payment not found")
    return payments.delete(db=db, item_id=payment_id)


##endpoints for reviews
@app.post("/reviews/", response_model=schemas.Review, tags=["Reviews"])
def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    return reviews.create(db=db, review=review)


@app.get("/reviews/", response_model=list[schemas.Review], tags=["Reviews"])
def read_reviews(db: Session = Depends(get_db)):
    return reviews.read_all(db)


@app.get("/reviews/{Review_id}", response_model=schemas.Review, tags=["Reviews"])
def read_one_review(review_id: int, db: Session = Depends(get_db)):
    review = reviews.read_one(db, item_id=review_id)
    if review is None:
        raise HTTPException(status_code=404, detail="Order detail not found")
    return review


@app.put("/reviews/{Review_id}", response_model=schemas.Review, tags=["Reviews"])
def update_one_review(Review_id: int, Review: schemas.ReviewUpdate, db: Session = Depends(get_db)):
    Review_db = reviews.read_one(db, item_id=Review_id)
    if Review_db is None:
        raise HTTPException(status_code=404, detail="Order detail not found")
    return reviews.update(db=db, request=Review, item_id=Review_id)


@app.delete("/reviews/{Review_id}", tags=["Reviews"])
def delete_one_review(Review_id: int, db: Session = Depends(get_db)):
    Review = reviews.read_one(db, item_id=Review_id)
    if Review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return reviews.delete(db=db, item_id=Review_id)


##endpoints for promos
@app.post("/promos/", response_model=schemas.Promo, tags=["Promos"])
def create_promo(promo: schemas.PromoCreate, db: Session = Depends(get_db)):
    return promos.create(db=db, promos=promo)


@app.get("/promos/", response_model=list[schemas.Promo], tags=["Promos"])
def read_promos(db: Session = Depends(get_db)):
    return promos.read_all(db)


@app.get("/promos/{promo_id}", response_model=schemas.Promo, tags=["Promos"])
def read_one_promo(promo_id: int, db: Session = Depends(get_db)):
    promo = promos.read_one(db, Promo_id=promo_id)
    if promo is None:
        raise HTTPException(status_code=404, detail="Promo not found")
    return promo


@app.put("/promos/{promo_id}", response_model=schemas.Promo, tags=["Promos"])
def update_one_promo(promo_id: int, promo: schemas.PromoUpdate, db: Session = Depends(get_db)):
     promo_db = promos.read_one(db, Promo_id=promo_id)
     if promo_db is None:
         raise HTTPException(status_code=404, detail="Promo not found")
     return promos.update(db=db, promo=promo, Promo_id=promo_id)


@app.delete("/promos/{promo_id}", tags=["Promos"])
def delete_one_promo(promo_id: int, db: Session = Depends(get_db)):
    promo = promos.read_one(db, Promo_id=promo_id)
    if promo is None:
        raise HTTPException(status_code=404, detail="Promo not found")
    return promos.delete(db=db, promo_id=promo_id)

