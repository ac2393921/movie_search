from logging import getLogger

from app.domain.entities.temp_user import TempUser
from app.domain.entities.user import User
from app.domain.repositories.temp_user.temp_user_repository import \
    TempUserRepository
from app.domain.repositories.user.user_repository import UserRepository
from app.domain.value_object.temp_user.confirm_code import ConfirmCode
from app.domain.value_object.temp_user.temp_user_id import TempUserId
from app.usecases.auth.register.input_port import RegisterInputPort
from app.usecases.auth.register.output_port import RegisterOutputPort

logger = getLogger("uvicorn.app")


class RegisterInteractor:
    def __init__(
        self,
        user_repository: UserRepository,
        temp_user_repository: TempUserRepository,
    ) -> None:
        self._user_repository = user_repository
        self._temp_user_repository = temp_user_repository

    def handle(self, input: RegisterInputPort):
        # 一時ユーザ情報を復元
        temp_user_id = TempUserId(value=input.temp_user_id)
        temp_user: TempUser = self._temp_user_repository.fetch_by_id(temp_user_id)

        # 確認コードをチェック
        temp_user.confirm(ConfirmCode(value=input.confirm_code))

        # 復元が成功したら一時ユーザ情報削除
        self._temp_user_repository.delete_by_id(temp_user_id)

        # 復元したユーザ情報を解析
        # DBに保存
        user = User.generate(
            username=temp_user.username.value,
            email=temp_user.email.value,
            password=temp_user.password.value,
        )
        user = self._user_repository.save(user)

        # JWTを作成

        return RegisterOutputPort(
            temp_user_id=str("aaaaa"),
        )
