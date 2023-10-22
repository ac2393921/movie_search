from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

user = "movie"
password = "movie"
host = "db"
db_name = "movie"

# engineの設定
engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{db_name}")

Base = declarative_base()
