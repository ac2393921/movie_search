from abc import ABC, abstractmethod

from app.domain.entities.temp_user import TempUser
from app.domain.value_object.temp_user.temp_user_id import TempUserId


class TempUserRepository(ABC):
    @abstractmethod
    def save(self, temp_user: TempUser) -> None:
        return NotImplementedError

    @abstractmethod
    def fetch_by_id(temp_user_id: TempUserId) -> TempUser:
        return NotImplementedError
    
    @abstractmethod
    def delete_by_id(self, temp_user_id: TempUserId) -> None:
        return NotImplementedError
