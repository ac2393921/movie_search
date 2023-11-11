from abc import ABC, abstractmethod

from app.domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    def fetch_by_email(self, email: str) -> User:
        return NotImplementedError
