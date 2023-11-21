from datetime import datetime, timedelta

from jose import jwt

from app.domain.domain_service.token_generator import TokenGenerator
from app.domain.entities.user import User


class TestTokenGenerator:
    def test_generate_token(self):
        # Arrange
        username = "testuser"
        user = User.generate(username, "test@email.com", "password")
        user_id = user.user_id.value
        
        assert isinstance(user, User)

        # Act
        token = TokenGenerator.generate_token(user)

        # Assert
        assert isinstance(token, str)

        # 内容を確認するためにデコードする
        decoded_token = jwt.decode(token, TokenGenerator.SECRET_KEY, algorithms=[TokenGenerator.ALGORITHM])
        assert decoded_token["user_id"] == user_id
        assert decoded_token["username"] == username

        # Check if the expiration is within the expected range
        # 期限が予想される範囲内にあるかどうかを確認します。
        expiration_time = datetime.utcfromtimestamp(decoded_token["exp"])
        assert expiration_time > datetime.utcnow()
        assert expiration_time < datetime.utcnow() + timedelta(days=90)
