from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    description: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Пирог с картошкой",
                "description": "Пирог приготовленный в печи с картошкой и луком.",
            }
        }


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True
