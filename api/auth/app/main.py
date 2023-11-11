from app.domain.repositories.user.user_repository import UserRepository
from app.infrastructures.database.handler.mysql_handler import MysplHandler, SqlHander
from app.infrastructures.database.repositories.user.mysql_user_repository import (
    MysqlUserRepository,
)
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Token(BaseModel):
    access_token: str
    token_type: str


class UserDomainService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    def exist_by_email(self, email: str):
        user = self._user_repository.fetch_by_email(email=email)

        if user is not None:
            raise Exception("ユーザーが既に存在しています")


class SignUpInputPort(BaseModel):
    username: str
    email: str
    password: str


class SignUpUseCase:
    def __init__(self, user_domain_service: UserDomainService) -> None:
        self._user_domain_service = user_domain_service

    def handle(self, input: SignUpInputPort):
        # 登録可能なメールか確認
        self._user_domain_service.exist_by_email(input.email)

        # パスワードハッシュ化

        # ユーザ情報をキャッシュに保存

        # キャッシュサーバーに保存するkeyの作成

        # キャッシュのサーバーに保存するvalueを作成

        # 保存

        # メール送信

        return


@app.post("/sign_up", response_model=Token)
async def sing_up(username: str, email: str, password: str):
    input = SignUpInputPort(
        username=username,
        email=email,
        password=password,
    )
    usecase = SignUpUseCase(
        user_domain_service=UserDomainService(
            user_repository=MysqlUserRepository(
                handler=MysplHandler(
                    host="db",
                    port=3306,
                    user="root",
                    password="movie",
                    db="users",
                )
            ),
        )
    )
    usecase.handle(input)

    return Token(access_token="xxx", token_type="bearer")
