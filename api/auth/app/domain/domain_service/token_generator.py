from datetime import datetime, timedelta

from jose import jwt

from app.domain.entities.user import User


class TokenGenerator:
    SECRET_KEY = "secret"
    ALGORITHM = "HS256"

    @classmethod
    def generate_token(cls, user: User):
        payload = {
            "exp": datetime.utcnow() + timedelta(days=90),
            "user_id": user.user_id.value,
            "username": user.username.value,
        }
        token = jwt.encode(payload, cls.SECRET_KEY, algorithm=cls.ALGORITHM)
        return token
