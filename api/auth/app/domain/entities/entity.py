from abc import abstractclassmethod

from pydantic import BaseModel


class Entity(BaseModel):
    class Config:
        frozen: False

    @abstractclassmethod
    def generate(cls):
        raise NotImplementedError()
