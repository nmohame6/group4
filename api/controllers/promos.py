from sqlmodel import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, promos):
    db_promos = models.Promos(
        discount=promos.discount
    )
    db.add(db_promos)
    db.commit()
    db.refresh(db_promos)
    return db_promos


def read_models(db: Session, promo_id):
    return db.query(models.Promos).filter(models.Promos.id == promo_id).all()