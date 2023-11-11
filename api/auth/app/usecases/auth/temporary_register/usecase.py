from abc import ABC, abstractmethod

from app.usecases.auth.temporary_register.input_port import TemporaryRegisterInputPort
from app.usecases.auth.temporary_register.output_port import TemporaryRegisterOutputPort


class TemporaryRegisterUseCase(ABC):
    @abstractmethod
    def handle(self, input: TemporaryRegisterInputPort) -> TemporaryRegisterOutputPort:
        return NotImplementedError
