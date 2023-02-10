import sqlite3
from contextlib import contextmanager
from psycopg2.extras import DictCursor
import psycopg2

@contextmanager
def conn_context(db_path: str):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    yield conn
    conn.close()


@contextmanager
def pg_conn_context(dsl: dict):
    pg_conn = psycopg2.connect(**dsl, cursor_factory=DictCursor)
    yield pg_conn
    pg_conn.close()


@contextmanager
def get_cursor(connection):
    cur = connection.cursor()
    yield cur
    cur.close()