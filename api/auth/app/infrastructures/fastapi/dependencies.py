from app.infrastructures.database.handler.mysql_handler import MysplHandler
from app.infrastructures.database.handler.redis_handler import RedisHandler
from app.infrastructures.database.repositories.temp_user.redis_temp_user_repository import (
    RedisTempUserRepository,
)
from app.infrastructures.database.repositories.user.mysql_user_repository import (
    MysqlUserRepository,
)
from app.interfaces.controllers.auth_controller import AuthController
from app.usecases.auth.temporary_register.interactor import TemporaryRegisterInteractor


def get_auth_controller() -> AuthController:
    return AuthController(
        temporary_register_usecase=TemporaryRegisterInteractor(
            user_repository=MysqlUserRepository(
                handler=MysplHandler(
                    host="db",
                    port=3306,
                    user="root",
                    password="movie",
                    db="users",
                )
            ),
            temp_user_repository=RedisTempUserRepository(
                handler=RedisHandler(
                    host="auth-redis",
                    port=6379,
                    db=0,
                )
            ),
        ),
    )
