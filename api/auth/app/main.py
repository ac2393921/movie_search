from logging import getLogger

from fastapi import Depends, FastAPI

from app.infrastructures.fastapi.dependencies import get_auth_controller
from app.interfaces.controllers.auth_controller import AuthController

logger = getLogger("uvicorn.app")
app = FastAPI()


@app.post("/temporary_register")
async def temporary_register(
    username: str,
    email: str,
    password: str,
    controller: AuthController = Depends(
        get_auth_controller,
    ),
):
    try:
        output = controller.temporary_register(username, email, password)
    except Exception as e:
        logger.error(e)
        return {"error": str(e)}

    return {"temp_user_id": output.temp_user_id}


@app.post("/register")
async def register(
    temp_user_id: str,
    confirm_code: str,
    controller: AuthController = Depends(
        get_auth_controller,
    ),
):
    try:
        output = controller.register(temp_user_id, confirm_code)
    except Exception as e:
        logger.error(e)
        return {"error": str(e)}

    return {"user": output.user, "token": output.token}


@app.post("/signin")
async def signin(
    email: str,
    password: str,
    controller: AuthController = Depends(
        get_auth_controller,
    ),
):
    try:
        output = controller.signin(email, password)
    except Exception as e:
        logger.error(e)
        return {"error": str(e)}

    return {"token": output.token}
