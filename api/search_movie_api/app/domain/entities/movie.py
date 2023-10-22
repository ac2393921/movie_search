from app.domain.entities.entity import Entity


class Movie(Entity):
    id: str
    title: str
    description: str
    release_date: str
    content_type: int
