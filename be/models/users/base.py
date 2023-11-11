from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

user = "movie"
password = "movie"
host = "db"
db_name = "users"

# engineの設定
engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{db_name}")

Base = declarative_base()
