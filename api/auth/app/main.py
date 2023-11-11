from app.infrastructures.fastapi.dependencies import get_auth_controller
from fastapi import Depends, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Token(BaseModel):
    access_token: str
    token_type: str


@app.post("/sign_up", response_model=Token)
async def sing_up(
    username: str,
    email: str,
    password: str,
    controller=Depends(
        get_auth_controller,
    ),
):
    output = controller.temporary_register(username, email, password)
    print(output)

    return Token(access_token="xxx", token_type="bearer")
