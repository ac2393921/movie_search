from app.domain.entities.entity import Entity


class User(Entity):
    id: str
    username: str
    email: str
    password: str
