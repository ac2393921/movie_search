from pydantic import BaseModel


class SingInOutputPort(BaseModel):
    token: str
