import os
import sqlite3

from psycopg2.extensions import connection as _connection

from sqlite import SQLiteLoader
from postgres import PostgresSaver
from db_conns import pg_conn_context, conn_context

from dotenv import load_dotenv

load_dotenv()

BATCH_SIZE = 100

CONFIG = {
    "POSTGRES_DBNAME": os.environ.get('DB_NAME'),
    "POSTGRES_USER": os.environ.get('DB_USER'),
    "POSTGRES_PASS": os.environ.get('DB_PASSWORD'),
    "POSTGRES_HOST": os.environ.get('DB_HOST'),
    "POSTGRES_PORT": os.environ.get('DB_PORT'),
    "SQLITE_PATH": os.path.join(os.getcwd(), os.environ.get('SQLITE_PATH')),
}


def load_from_sqlite(connection: sqlite3.Connection, pg_connect: _connection):
    """Основной метод загрузки данных из SQLite в Postgres"""

    postgres_saver = PostgresSaver(pg_connect)
    sqlite_loader = SQLiteLoader(connection)

    tables = sqlite_loader.get_tables()
    for table in tables:
        data_gen = sqlite_loader.load_table_gen(table, batch_size=BATCH_SIZE)
        postgres_saver.save_all_data(data_gen, table)


if __name__ == '__main__':
    dsl = {'dbname': CONFIG['POSTGRES_DBNAME'], 'user': CONFIG['POSTGRES_USER'],
           'password': CONFIG['POSTGRES_PASS'], 'host': CONFIG['POSTGRES_HOST'],
           'port': CONFIG['POSTGRES_PORT']}
    with conn_context('db.sqlite') as sqlite_conn, \
            pg_conn_context(dsl) as pg_conn:
        load_from_sqlite(sqlite_conn, pg_conn)
