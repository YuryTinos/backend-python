from abc import ABC, abstractmethod
from typing import List
from src.domain.models import User


class UserRepositoryInterface(ABC):
    """Interface to Pet Repository"""

    @abstractmethod
    def insert_user(cls, name: str, password: str) -> User:
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def select_user(cls, user_id: int = None, name: str = None) -> List[User]:
        raise NotImplementedError("Method not implemented")
