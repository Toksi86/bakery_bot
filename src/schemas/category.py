from typing import Optional

from pydantic import BaseModel


class Category(BaseModel):
    id: int
    name: str
    description: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Пирог с картошкой",
                "description": "Пирог приготовленный в печи с картошкой и луком.",
            }
        }
