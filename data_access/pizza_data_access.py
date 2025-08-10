import sqlite3
import os

class BaseDataAccess:
    def __init__(self, connection_str: str = None):
        if connection_str:
            self._connection_str = connection_str
        else:
            self._connection_str = os.environ.get("DB_FILE")
            if self._connection_str is None:
                raise Exception("DB_FILE environment variable or parameter connection_str has to be set.")

    def _connect(self):
        return sqlite3.connect(self._connection_str, detect_types=sqlite3.PARSE_DECLTYPES)

    def fetchone(self, sql: str, params: tuple = None):
        if params is None:
            params = ()
        with self._connect() as conn:
            try:
                cursor = conn.execute(sql, params)
                return cursor.fetchone()
            except sqlite3.Error as e:
                conn.rollback()
                raise e

    def fetchall(self, sql: str, params: tuple = None):
        if params is None:
            params = ()
        with self._connect() as conn:
            try:
                cursor = conn.execute(sql, params)
                return cursor.fetchall()
            except sqlite3.Error as e:
                conn.rollback()
                raise e

    def execute(self, sql: str, params: tuple = None):
        if params is None:
            params = ()
        with self._connect() as conn:
            try:
                cursor = conn.execute(sql, params)
                conn.commit()
                return cursor.lastrowid, cursor.rowcount
            except sqlite3.Error as e:
                conn.rollback()
                raise e
