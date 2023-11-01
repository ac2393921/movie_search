from typing import List

from app.domain.entities.movie import Movie
from app.domain.entities.search_result import SearchResult
from app.domain.repositories.search_result.search_result_repository_if import (
    SearchResultRepositoryIf,
)
from app.infrastructures.database.handler.search_engine_handler import (
    SearchEngineHandler,
)


class ElasticSearchQueryBuilder:
    def __init__(self):
        self._query = {}

    def build_match_query(self, field, value):
        return {"match": {field: value}}

    def build_nested_query(self, path, nested_field, value):
        return {
            "nested": {
                "path": path,
                "query": {"match": {f"{path}.{nested_field}": value}},
            }
        }

    def build_bool_query(self, must=None, must_not=None, should=None):
        bool_query = {"bool": {}}

        if must:
            bool_query["bool"]["must"] = must
        if must_not:
            bool_query["bool"]["must_not"] = must_not
        if should:
            bool_query["bool"]["should"] = should
        if filter:
            bool_query["bool"]["filter"] = filter

        self._query["query"] = bool_query

        return self._query


class SearchQueryBuilder(ElasticsearchQueryBuilder):
    def __init__(self):
        self._should_queries = []
        self._must_queries = []
        self._must_not_queries = []

    def build_query(self, keyword=None):
        self._should_queries = []
        if keyword:
            self.build_match_query("title", keyword)
        self._should_queries.append(self.build_match_query("title", keyword))
        if keyword:
            self.build_match_query("description", keyword)

        if keyword:
            self.build_nested_query("genres", "name", keyword)

        if keyword:
            self.build_match_query("director.name", keyword)

        if keyword:
            self.build_nested_query("casts", "name", keyword)

        if keyword:
            self.build_nested_query("production_countries", "name", keyword)

        if keyword:
            self.build_function_score_query("score")

        query = {"query": {"bool": {"should": should_queries}}}

        return query


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
        es_results = self._handler.search(index="movies", query=query, size=100)["hits"]

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
