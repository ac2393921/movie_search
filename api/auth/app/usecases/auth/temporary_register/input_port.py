from pydantic import BaseModel


class TemporaryRegisterInputPort(BaseModel):
    username: str
    email: str
    password: str
