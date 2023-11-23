from typing import Optional

from app.domain.entities.user import User
from app.domain.repositories.user.user_repository import UserRepository
from app.infrastructures.database.handler.mysql_handler import (MysplHandler,
                                                                SqlHander)


class MysqlUserRepository(UserRepository):
    def __init__(self, handler: SqlHander):
        self._handler = handler

    def fetch_by_email(self, email: str) -> Optional[User]:
        user = None

        query = "SELECT * FROM users WHERE email = %s"

        with self._handler as _:
            results_with_where = self._handler.execute_query(query, email)
            for row in results_with_where:
                user = User.regenerate(
                    user_id=row["id"],
                    username=row["username"],
                    email=row["email"],
                    password=row["password"],
                )
        return user

    def save(self, user: User) -> None:
        query = "INSERT INTO users (id, username, email, password) VALUES (%s, %s, %s, %s)"

        with self._handler as _:
            self._handler.execute_command(
                query, (user.user_id.value, user.username.value, user.email.value, user.password.decode())
            )
