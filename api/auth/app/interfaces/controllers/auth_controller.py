from app.usecases.auth.temporary_register.input_port import TemporaryRegisterInputPort
from app.usecases.auth.temporary_register.usecase import TemporaryRegisterUseCase


class AuthController:
    def __init__(self, temporary_register_usecase: TemporaryRegisterUseCase) -> None:
        self._temporary_register_usecase = temporary_register_usecase

    def temporary_register(self, username: str, email: str, password: str):
        input = TemporaryRegisterInputPort(
            username=username, email=email, password=password
        )
        output = self._temporary_register_usecase.handle(input)
        return output
