from app.infrastructures.database.handler.elastic_search_handler import (
    ElasticSearchHandler,
)
from app.infrastructures.database.repositories.es_search_result_impl import (
    EsSearchResultRepositoryImpl,
)
from app.interfaces.controllers.movie_controller import MovieController
from app.usecases.search.search_movie_interactor import SearchMovieInteractor


def get_movie_controller() -> MovieController:
    return MovieController(
        search_movie_usecase=SearchMovieInteractor(
            search_result_repository=EsSearchResultRepositoryImpl(
                handler=ElasticSearchHandler(es_host="elasticsearch", es_port="9200")
            )
        )
    )
