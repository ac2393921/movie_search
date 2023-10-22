from pydantic import BaseModel


class SearchMovieInputPort(BaseModel):
    keyword: str
