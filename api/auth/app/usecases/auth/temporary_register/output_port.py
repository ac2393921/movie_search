from pydantic import BaseModel


class TemporaryRegisterOutputPort(BaseModel):
    username: str
    email: str
    password: str
