from pydantic import BaseModel


class Entity(BaseModel):
    class Config:
        frozen: False
