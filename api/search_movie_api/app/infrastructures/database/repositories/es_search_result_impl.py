from typing import List

from app.domain.entities.movie import Movie
from app.domain.entities.search_result import SearchResult
from app.domain.repositories.search_result.search_result_repository_if import (
    SearchResultRepositoryIf,
)
from app.infrastructures.database.handler.search_engine_handler import (
    SearchEngineHandler,
)


class EsSearchResultRepositoryImpl(SearchResultRepositoryIf):
    def __init__(self, handler: SearchEngineHandler) -> None:
        self._handler = handler

    def search(self, keyword: str) -> SearchResult:
        id = f"movie_{keyword}"

        query = {
            "query": {
                "bool": {
                    "should": [
                        {"match": {"title": keyword}},
                        {"match": {"description": keyword}},
                        {
                            "nested": {
                                "path": "genres",
                                "query": {"match": {"genres.name": keyword}},
                            }
                        },
                        {"match": {"director.name": keyword}},
                        {
                            "nested": {
                                "path": "casts",
                                "query": {"match": {"casts.name": keyword}},
                            }
                        },
                        {
                            "nested": {
                                "path": "production_countries",
                                "query": {
                                    "match": {"production_countries.name": keyword}
                                },
                            }
                        },
                        {
                            "function_score": {
                                "field_value_factor": {"field": "score", "missing": 0}
                            }
                        },
                    ]
                }
            }
        }
        es_results = self._handler.search(index="movies", query=query)["hits"]

        movies: List[Movie] = []
        for es_result in es_results["hits"]:
            source = es_result["_source"]
            movie = Movie(
                id=source["id"],
                title=source["title"],
                description=source["description"],
                release_date=source["release_date"],
                content_type=source["content_type"],
            )
            movies.append(movie)

        search_result = SearchResult(
            id=id, movies=movies, total_hits=es_results["total"]["value"]
        )

        return search_result
