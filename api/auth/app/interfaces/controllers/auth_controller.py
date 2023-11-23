from app.usecases.auth.register.input_port import RegisterInputPort
from app.usecases.auth.register.usecase import RegisterUseCase
from app.usecases.auth.sign_in.input_port import SingInInputPort
from app.usecases.auth.sign_in.usecase import SingInUseCase
from app.usecases.auth.temporary_register.input_port import \
    TemporaryRegisterInputPort
from app.usecases.auth.temporary_register.usecase import \
    TemporaryRegisterUseCase


class AuthController:
    def __init__(self, temporary_register_usecase: TemporaryRegisterUseCase, register_usecase: RegisterUseCase, signin_usecase: SingInUseCase) -> None:
        self._temporary_register_usecase = temporary_register_usecase
        self._register_usecase = register_usecase
        self._signin_usecase = signin_usecase

    def temporary_register(self, username: str, email: str, password: str):
        input = TemporaryRegisterInputPort(
            username=username, email=email, password=password
        )
        output = self._temporary_register_usecase.handle(input)
        return output

    def register(self, temp_user_id: str, confirm_code: str):
        input = RegisterInputPort(
            temp_user_id=temp_user_id, confirm_code=confirm_code,
        )
        output = self._register_usecase.handle(input)
        return output

    def signin(self, email: str, password: str):
        input = SingInInputPort(email=email, password=password)
        output = self._signin_usecase.handle(input)
        return output
