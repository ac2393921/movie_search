from abc import ABC, abstractmethod
from typing import Optional

from app.domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    def fetch_by_email(self, email: str) -> Optional[User]:
        return NotImplementedError

    @abstractmethod
    def save(self, user: User) -> None:
        return NotImplementedError
