from pydantic import BaseModel


class TemporaryRegisterOutputPort(BaseModel):
    temp_user_id: str
