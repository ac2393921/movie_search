from app.infrastructures.fastapi.dependencies import get_movie_controller
from app.interfaces.controllers.movie_controller import MovieController
from fastapi import Depends, FastAPI

app = FastAPI()


@app.get("/search")
async def search(
    keyword: str, controller: MovieController = Depends(get_movie_controller)
):
    response = controller.search(keyword)

    return {"results": response}
