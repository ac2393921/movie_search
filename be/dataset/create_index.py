from logging import getLogger

from elasticsearch import Elasticsearch, helpers
from pydantic import BaseSettings, Field
from sqlalchemy.orm import joinedload

from be.dataset.create_movie_data import create_session_handler
from be.models.movie import Movie

logger = getLogger(__name__)


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
            "id": {"type": "keyword"},
            "title": {"type": "text"},
            "description": {"type": "text"},
            "genres": {
                "type": "nested",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "text", "analyzer": "standard"},
                },
            },
            "casts": {
                "type": "nested",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "text", "analyzer": "standard"},
                },
            },
            "production_countries": {
                "type": "nested",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "text", "analyzer": "standard"},
                },
            },
            "director": {
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "text", "analyzer": "standard"},
                },
            },
            "content_type": {"type": "integer"},
            "release_date": {"type": "date"},
            "score": {"type": "float"},
        },
    }
}


def gendata(movie_list):
    es_movies = []

    for movie in movie_list:
        movie_dict = {
            "id": movie.id,
            "title": movie.title,
            "description": movie.description,
            "genres": [{"id": genre.id, "name": genre.name} for genre in movie.genres],
            "casts": [{"id": cast.id, "name": cast.name} for cast in movie.casts],
            "production_countries": [
                {"id": production_country.id, "name": production_country.name}
                for production_country in movie.productin_countries
            ],
            "release_date": movie.release_date,
            "score": movie.score,
        }

        if movie.director:
            movie_dict["director"] = {
                "id": movie.director.id,
                "name": movie.director.name,
            }

        if movie.content_type:
            movie_dict["content_type"] = movie.content_type.id

        es_movies.append(movie_dict)

    for movie in es_movies:
        yield {"_op_type": "create", "_index": "movies", "_source": movie}


if __name__ == "__main__":
    logger.info("Movieインデックスを作成します")
    session_handler = create_session_handler(
        user="movie",
        password="movie",
        host="db",
        db_name="movie",
    )
    session = session_handler.get_session()
    movie_list = (
        session.query(Movie)
        .options(joinedload(Movie.director))
        .options(joinedload(Movie.content_type))
        .options(joinedload(Movie.genres))
        .options(joinedload(Movie.casts))
        .options(joinedload(Movie.productin_countries))
        .all()
    )

    try:
        es.indices.create(index="movies", body=mapping)
    except Exception as e:
        pass

    helpers.bulk(es, gendata(movie_list))
