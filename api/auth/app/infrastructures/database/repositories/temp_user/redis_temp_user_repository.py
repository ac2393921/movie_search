from app.domain.entities.temp_user import TempUser
from app.domain.repositories.temp_user.temp_user_repository import TempUserRepository
from app.infrastructures.database.handler.redis_handler import RedisHandler


class RedisTempUserRepository(TempUserRepository):
    def __init__(self, handler: RedisHandler):
        self._handler = handler

    def save(self, temp_user: TempUser):
        self._handler.set_value(
            key=temp_user.temp_user_id.value,
            value=str(temp_user),
            ex=60 * 60 * 24,
        )
