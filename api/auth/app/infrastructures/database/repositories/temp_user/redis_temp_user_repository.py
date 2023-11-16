from app.domain.entities.temp_user import TempUser
from app.domain.repositories.temp_user.temp_user_repository import \
    TempUserRepository
from app.domain.value_object.temp_user.temp_user_id import TempUserId
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

    def fetch_by_id(self, temp_user_id: TempUserId) -> TempUser:
        value = self._handler.get_value(temp_user_id.value)

        if value in [None, ""]:
            raise Exception("temp user is not found")

        values = value.split(" ")

        temp_user = TempUser.regenarate(
            temp_user_id=values[0],
            username=values[1],
            email=values[2],
            password=values[3],
            confirm_code=values[4],
        )

        return temp_user

    def delete_by_id(self, temp_user_id: TempUserId):
        self._handler.delete_key(temp_user_id.value)

