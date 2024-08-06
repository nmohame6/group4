from sqlalchemy.orm import Session
from fastapi import status, Response
from ..models import models


def create(db: Session, request):

    db_recipe = models.Recipe(
        sandwich_id=request.sandwich_id,
        resource_id = request.resource_id,
        amount= request.amount
    )

    db.commit()

    db.refresh(db_recipe)

    return db_recipe


def read_all(db: Session):
    return db.query(models.Recipe).all()


def read_one(db: Session, recipe_id):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()


def update(db: Session, recipe_id, recipe):
 
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)

    update_data = recipe.model_dump(exclude_unset=True)

    db_recipe.update(update_data, synchronize_session=False)

    db.commit()

    return db_recipe.first()


def delete(db: Session, recipe_id):

    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)

    db_recipe.delete(synchronize_session=False)
 
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)