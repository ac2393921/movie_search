from typing import Any

from pydantic import BaseModel


class ValueObject(BaseModel):
    value: Any

    class Config:
        frozen: True

    def __str__(self) -> str:
        return str(self.value)
