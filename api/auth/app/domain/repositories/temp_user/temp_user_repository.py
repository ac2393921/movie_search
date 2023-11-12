from abc import ABC, abstractmethod

from app.domain.entities.temp_user import TempUser


class TempUserRepository(ABC):
    @abstractmethod
    def save(self, temp_user: TempUser) -> None:
        return NotImplementedError
