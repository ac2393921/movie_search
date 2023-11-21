from typing import Any

from pydantic import BaseModel

from app.domain.entities.user import User


class RegisterOutputPort(BaseModel):
    user: Any
    token: str
