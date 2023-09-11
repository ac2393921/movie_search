from elasticsearch import Elasticsearch
from fastapi import FastAPI

app = FastAPI()


@app.get("/search")
async def root(keyword: str):
    es = Elasticsearch("http://elasticsearch:9200")

    query = {
        "query": {
            "match": {
                "title": keyword,
            }
        }
    }
    SearchResult = es.search(index="movies", body=query, size=5)
    return {"message": SearchResult}
