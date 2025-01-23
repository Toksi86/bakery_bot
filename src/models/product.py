from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.core.db import Base
from src.models.category import Category


class Product(Base):
    name = Column(String, nullable=False)
    description = Column(String)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)

    def __repr__(self):
        return f"Product(name='{self.name}', description='{self.description}')"

    def __str__(self):
        return f"{self.name}: {self.description}"
