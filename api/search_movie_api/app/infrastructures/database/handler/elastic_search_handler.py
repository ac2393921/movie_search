from typing import Optional

from app.infrastructures.database.handler.search_engine_handler import (
    SearchEngineHandler,
)
from elasticsearch import Elasticsearch


class ElasticSearchHandler(SearchEngineHandler):
    def __init__(self, es_host: str, es_port: str = None) -> None:
        self._es_host = es_host
        self._es_port = es_port

    def get_client(self) -> Elasticsearch:
        return Elasticsearch("http://elasticsearch:9200")
        # return Elasticsearch([{"host": self._es_host, "port": self._es_port}])

    def search(self, index, query, size=100):
        es_client = self.get_client()
        result = es_client.search(index=index, body=query, size=size)
        return result
