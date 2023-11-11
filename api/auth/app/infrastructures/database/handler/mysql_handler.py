from abc import ABC, abstractmethod

import pymysql


class SqlHander(ABC):
    @abstractmethod
    def execute_query(self, query, params=None):
        return NotImplementedError


class MysplHandler(SqlHander):
    def __init__(self, host, port, user, password, db):
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._db = db

    def __enter__(self):
        self._conn = pymysql.connect(
            host=self._host,
            port=self._port,
            user=self._user,
            password=self._password,
            db=self._db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )
        return self._conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conn.close()

    def execute_query(self, query, params=None):
        cursor = self._conn.cursor()
        try:
            cursor.execute(query, params)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error executing query: {e}")
        finally:
            cursor.close()
