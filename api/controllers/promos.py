from sqlalchemy.orm import Session
from fastapi import status, Response
from ..models import models


def create(db: Session, promos):
    db_promos = models.Promo(
        promo_id=promos.promo_id,
        discount=promos.discount,
        expiration=promos.expiration

    )
    db.add(db_promos)
    db.commit()
    db.refresh(db_promos)
    return db_promos


def read_all(db: Session):
    return db.query(models.Promo).all()


def read_one(db: Session, Promo_id):
    return db.query(models.Promo).filter(models.Promo.id == Promo_id).first()


def update(db: Session, Promo_id, promo):

    db_promo = db.query(models.Promo).filter(models.Promo.id == Promo_id)

    update_data = promo.model_dump(exclude_unset=True)

    db_promo.update(update_data, synchronize_session=False)

    db.commit()

    return db_promo.first()


def delete(db: Session, promo_id):

    db_promo = db.query(models.Promo).filter(models.Promo.id == promo_id)

    db_promo.delete(synchronize_session=False)

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)