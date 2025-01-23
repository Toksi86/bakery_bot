from sqlalchemy import Column, String, Text

from src.core.db import Base


class Category(Base):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)

    def __repr__(self):
        return f"Category(name='{self.name}', description='{self.description}')"

    def __str__(self):
        return f"{self.name}: {self.description}"
