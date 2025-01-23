from typing import Optional

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: Optional[str]
    category_id: int

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Выпечка",
                "description": "Товары из категории Выпечка",
                "category_id": 2,
            }
        }


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    category_id: int

    class Config:
        orm_mode = True
