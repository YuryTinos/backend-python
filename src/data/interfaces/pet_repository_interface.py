from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Pet


class PetRepositoryInterface(ABC):
    """Interface to Pet Repository"""

    @abstractmethod
    def insert_pet(cls, name: str, species: str, age: int, user_id: int) -> Pet:
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def select_pet(cls, pet_id: int = None, user_id: int = None) -> List[Pet]:
        raise NotImplementedError("Method not implemented")
