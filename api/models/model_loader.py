from . import orders, order_details, recipes, sandwiches, resources, payments, reviews, promos

from ..dependencies.database import engine
from ..dependencies.database import Base


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    payments.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)
    promos.Base.metadata.create_all(engine)
