import enum
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from src.infra.config import Base


class AnimalTypes(enum.Enum):
    """Defining Animals Types"""

    dog = "dog"
    cat = "cat"
    fish = "fish"
    turtle = "turtle"


class Pets(Base):
    """Pets Entity"""

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    species = Column(Enum(AnimalTypes), nullable=False)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __rep__(self):
        return f"Pets [name={self.name}, specie={self.species}, user_id={self.user_id}]"
