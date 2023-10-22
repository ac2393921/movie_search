from abc import ABC, abstractmethod

from app.usecases.search.search_movie_input_port import SearchMovieInputPort
from app.usecases.search.search_movie_output_port import SearchMovieOutputPort


class SearchMovieUsecase(ABC):
    @abstractmethod
    def search(self, input: SearchMovieInputPort) -> SearchMovieOutputPort:
        raise NotImplementedError
