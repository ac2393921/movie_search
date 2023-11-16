from pydantic import BaseModel


class RegisterInputPort(BaseModel):
    temp_user_id: str
    confirm_code: str
