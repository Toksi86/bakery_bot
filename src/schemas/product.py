from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    description: str = ""
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
