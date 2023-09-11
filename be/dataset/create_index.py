import csv

from elasticsearch import Elasticsearch, helpers
from pydantic import BaseSettings, Field

from api.dataset.create_movie_data import create_session_handler
from api.models.movie import Movie


class OpenSearchConnectnionSeetings(BaseSettings):
    host: str = Field(env="OPEN_SEARCH_HOST", default="localhost")
    port: int = Field(env="OPEN_SEARCH_PORT", default=9200)
    use_ssl: bool = Field(env="OPEN_SEARCH_USE_SSL", default=True)
    verify_certs: bool = Field(env="OPEN_SEARCH_VERIFY_CERTS", default=True)
    ssl_show_warn: bool = False


opensearch_connection_settings = OpenSearchConnectnionSeetings()

es = Elasticsearch("http://elasticsearch:9200")
# es = Elasticsearch(
#     hosts=[opensearch_connection_settings.host],
#     port=opensearch_connection_settings.port,
#     use_ssl=opensearch_connection_settings.use_ssl,
#     ssl_show_warn=opensearch_connection_settings.ssl_show_warn,
#     verify_certs=opensearch_connection_settings.verify_certs,
# )

mapping = {
    "mappings": {
        "properties": {
            "title": {"type": "text"},
            "description": {"type": "text"},
        },
    }
}


# with open("./data/movies.csv", encoding="utf-8") as f:
#     reader = csv.DictReader(f)
#     helpers.bulk(es, reader, index="movies")
# helpers.bulk(es, reader, index="movies", doc_type="movie")


def gendata(movie_list):
    es_movies = []

    for movie in movie_list:
        es_movies.append(
            {
                "title": movie.title,
                "description": movie.description,
            },
        )

    for movie in es_movies:
        yield {"_op_type": "create", "_index": "movies", "_source": movie}


if __name__ == "__main__":
    session_handler = create_session_handler(
        user="movie",
        password="movie",
        host="db",
        db_name="movie",
    )
    session = session_handler.get_session()
    movie_list = session.query(Movie.title, Movie.description).all()

    try:
        es.indices.create(index="movies", body=mapping)
    except Exception as e:
        pass

    helpers.bulk(es, gendata(movie_list))
