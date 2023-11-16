from pydantic import BaseModel


class RegisterOutputPort(BaseModel):
    temp_user_id: str
