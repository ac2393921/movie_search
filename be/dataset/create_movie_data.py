import datetime
import math

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from be.models.base import Base
from be.models.cast import Cast
from be.models.cast_movie import CastMovie
from be.models.content_type import ContentType
from be.models.director import Director
from be.models.genre import Genre
from be.models.genre_movie import GenreMovie
from be.models.movie import Movie
from be.models.movie_porduction_country import MovieProductionCountry
from be.models.production_country import ProductionCountry


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
    def __init__(self, engine, session, path: str) -> None:
        self._engine = engine
        self._session = session
        self._df = self.load_csv_data(path)

    def load_csv_data(self, path) -> pd.DataFrame:
        df = pd.read_csv(path)
        return df

    def create_data(self) -> None:
        self._create_table()
        self._create_production_country()
        self._create_content_type()
        self._create_director()
        self._create_cast()
        self._create_genre()
        self._create_movie()
        self._create_genre_movie()
        self._create_cast_movie()
        self._create_movie_production_country()

    def _create_table(self) -> None:
        # テーブルを作成する
        Base.query = self._session.query_property()
        Base.metadata.create_all(bind=self._engine)

    def _create_production_country(self) -> None:
        print("Create Production Country")
        unique_country = set()
        for row in self._df["Production Country"].dropna():
            country_list = row.split(", ")
            for country in country_list:
                unique_country.add(country)

        for country in unique_country:
            if country == "":
                continue
            country = ProductionCountry(name=country)
            self._session.add(country)

        self._session.commit()

    # Create ContentType
    def _create_content_type(self) -> None:
        print("Create ContentType")
        for row in self._df["Content Type"].dropna().unique():
            content_type = ContentType(name=row)

            self._session.add(content_type)
        self._session.commit()

    # Create Director
    def _create_director(self) -> None:
        print("Create Director")
        d = []
        for row in self._df["Director"].dropna():
            row = row.title()
            if row in d:
                continue
            d.append(row)
            director = None
            director = Director(name=row)

            self._session.add(director)
        self._session.commit()

    def _create_cast(self) -> None:
        print("Create Cast")
        unique_cast = set()
        for row in self._df["Cast"].dropna():
            casts_list = row.split(", ")
            for cast in casts_list:
                cast = cast.title()
                unique_cast.add(cast)

        for cast in unique_cast:
            cast = Cast(name=cast)
            self._session.add(cast)
        self._session.commit()

    def _create_genre(self):
        print("Create Genre")
        unique_genre = set()
        for row in self._df["Genres"]:
            genres_list = row.split(", ")
            for genre in genres_list:
                unique_genre.add(genre)

        for genre in unique_genre:
            genre = Genre(name=genre)
            self._session.add(genre)
        self._session.commit()

    def _create_movie(self) -> None:
        print("Create Movie")
        for row in self._df.itertuples():
            id = row[1]
            title = row[2]
            descriprion = row[3]
            director = row[4]
            release_date = row[8]
            score = row[11]
            content_type = row[12]

            director_id = None
            if type(director) == str:
                director_id = (
                    self._session.query(Director)
                    .filter(Director.name == director)
                    .first()
                    .id
                )

            content_type_id = None
            if type(content_type) == str:
                content_type_id = (
                    self._session.query(ContentType)
                    .filter(ContentType.name == content_type)
                    .first()
                    .id
                )

            if not math.isnan(release_date):
                release_date = datetime.datetime.strptime(str(int(release_date)), "%Y")
            else:
                release_date = None

            if type(score) == str:
                score = float(row[11].replace("/10", ""))
            else:
                score = None

            movie = Movie(
                id=id,
                director_id=director_id,
                content_type_id=content_type_id,
                title=title,
                description=descriprion,
                release_date=release_date,
                score=score,
            )
            self._session.add(movie)
        self._session.commit()

    def _create_genre_movie(self) -> None:
        print("Create GenreMovie")
        for row in self._df.itertuples():
            id = row[1]
            genres = row[5]
            genres = genres.split(", ")

            genre_list = self._session.query(Genre).filter(Genre.name.in_(genres)).all()

            for genre in genre_list:
                genre_movie = GenreMovie(movie_id=id, genre_id=genre.id)
                self._session.add(genre_movie)
        self._session.commit()

    def _create_movie_production_country(self) -> None:
        print("Create MovieProductionCountry")
        for row in self._df.itertuples():
            id = row[1]
            production_countries = row[7]
            if type(production_countries) == float:
                continue
            production_countries = production_countries.split(", ")

            production_countory_list = (
                self._session.query(ProductionCountry)
                .filter(ProductionCountry.name.in_(production_countries))
                .all()
            )

            for production_countory in production_countory_list:
                movie_production_countory = MovieProductionCountry(
                    movie_id=id, production_country_id=production_countory.id
                )
                self._session.add(movie_production_countory)
        self._session.commit()

    def _create_cast_movie(self) -> None:
        print("Create CastMovie")
        for row in self._df.itertuples():
            id = row[1]
            casts = row[6]
            if type(casts) == float:
                continue
            casts = casts.split(", ")

            cast_list = self._session.query(Cast).filter(Cast.name.in_(casts)).all()

            for cast in cast_list:
                cast_movie = CastMovie(movie_id=id, cast_id=cast.id)
                self._session.add(cast_movie)
            self._session.commit()


if __name__ == "__main__":
    session_handler = create_session_handler(
        user="movie",
        password="movie",
        host="db",
        db_name="movie",
    )
    data_manager = DBDataManager(
        session_handler.get_engine(),
        session_handler.get_session(),
        "data/netflixData.csv",
    )
    data_manager.create_data()
