from abc import ABC, abstractmethod

from app.usecases.auth.sign_in.input_port import SingInInputPort
from app.usecases.auth.sign_in.output_port import SingInOutputPort


class SingInUseCase(ABC):
    @abstractmethod
    def handle(self, input: SingInInputPort) -> SingInOutputPort:
        return NotImplementedError
