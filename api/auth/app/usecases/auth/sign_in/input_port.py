from pydantic import BaseModel


class SingInInputPort(BaseModel):
    email: str
    password: str
