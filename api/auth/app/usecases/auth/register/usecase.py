from abc import ABC, abstractmethod

from app.usecases.auth.register.input_port import RegisterInputPort
from app.usecases.auth.register.output_port import RegisterOutputPort


class RegisterUseCase(ABC):
    @abstractmethod
    def handle(self, input: RegisterInputPort) -> RegisterOutputPort:
        return NotImplementedError
