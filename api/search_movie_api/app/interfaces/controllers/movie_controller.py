from app.usecases.search.search_movie_input_port import SearchMovieInputPort
from app.usecases.search.search_movie_usecase import SearchMovieUsecase


class MovieController:
    def __init__(self, search_movie_usecase: SearchMovieUsecase) -> None:
        self._search_movie_usecase = search_movie_usecase

    def search(self, keyword: str):
        input = SearchMovieInputPort(keyword=keyword)
        output = self._search_movie_usecase.search(input)
        return output
