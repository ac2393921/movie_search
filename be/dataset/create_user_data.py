from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from be.models.users.base import Base
from be.models.users.user import User


class SessionHandler:
    def __init__(self, engine, session) -> None:
        self._session = session
        self._engine = engine

    def get_engine(self):
        return self._engine

    def get_session(self):
        return self._session


def create_session_handler(
    user, password: str, host: str, db_name: str
) -> SessionHandler:
    # engineの設定
    engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{db_name}")

    # セッションの作成
    db_session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )

    return SessionHandler(engine, db_session)


class DBDataManager:
    def __init__(self, engine, session) -> None:
        self._engine = engine
        self._session = session

    def _create_table(self) -> None:
        # テーブルを作成する
        Base.query = self._session.query_property()
        Base.metadata.create_all(bind=self._engine)

    def create_data(self) -> None:
        self._create_table()


if __name__ == "__main__":
    session_handler = create_session_handler(
        user="root",
        password="movie",
        host="db",
        db_name="users",
    )
    data_manager = DBDataManager(
        session_handler.get_engine(),
        session_handler.get_session(),
    )
    data_manager.create_data()
