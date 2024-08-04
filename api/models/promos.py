class PromosCreate(PromosBase):
    pass


class PromosUpdate(BaseModel):
    discount: Optional[int] = None
    expirydate: Optional[datetime] = None

class Promo(PromoBase):
    discount = Optional[int] = None

    class ConfigDict:
        from_attributes = True
