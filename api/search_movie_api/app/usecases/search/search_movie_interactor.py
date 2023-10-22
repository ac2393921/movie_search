from app.domain.repositories.search_result.search_result_repository_if import (
    SearchResultRepositoryIf,
)
from app.usecases.search.search_movie_input_port import SearchMovieInputPort
from app.usecases.search.search_movie_output_port import SearchMovieOutputPort
from app.usecases.search.search_movie_usecase import SearchMovieUsecase


class SearchMovieInteractor(SearchMovieUsecase):
    def __init__(self, search_result_repository: SearchResultRepositoryIf) -> None:
        self._movie_repository = search_result_repository

    def search(self, input: SearchMovieInputPort) -> SearchMovieOutputPort:
        result = self._movie_repository.search(input.keyword)
        return SearchMovieOutputPort(
            movies=result.movies,
            total_hits=result.total_hits,
        )
