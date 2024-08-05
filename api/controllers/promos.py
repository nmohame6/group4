from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, promos):
    db_promos = models.Promo(
        discount=promos.discount
    )
    db.add(db_promos)
    db.commit()
    db.refresh(db_promos)
    return db_promos


def read_models(db: Session, promo_id):
    return db.query(models.Promo).filter(models.Promo.id == promo_id).all()