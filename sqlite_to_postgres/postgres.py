from psycopg2.extras import execute_batch
from datetime import datetime


class PostgresSaver:

    def __init__(self, connection) -> None:
        self.connection = connection

    def save_all_persons(self, data: list, n: int = 16) -> None:
        with self.connection.cursor() as cur:
            query = 'INSERT INTO content.person (id, full_name, created, modified) \
                VALUES (%s, %s, %s, %s) ON CONFLICT (id) DO NOTHING; '
            insert_data = [(p.id, p.full_name, p.created_at, datetime.now())
                           for p in data]
            execute_batch(cur, query, insert_data, page_size=n)
            self.connection.commit()

    def save_all_filmworks(self, data: list, n: int = 16) -> None:
        with self.connection.cursor() as cur:
            query = 'INSERT INTO content.film_work (id, title, created, modified, description, creation_date, rating, type) \
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING; '
            insert_data = [
                (m.id, m.title, m.created_at, datetime.now(), m.description, m.creation_date, m.rating, m.type)
                for m in data]
            execute_batch(cur, query, insert_data, page_size=n)
            self.connection.commit()

    def save_all_genres(self, data: list, n: int = 16) -> None:
        with self.connection.cursor() as cur:
            query = 'INSERT INTO content.genre (id, name, description, created, modified) \
                VALUES (%s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING; '
            insert_data = [(g.id, g.name, g.description, g.created_at, datetime.now())
                           for g in data]
            execute_batch(cur, query, insert_data, page_size=n)
            self.connection.commit()

    def save_all_genre_filmworks(self, data: list, n: int = 16) -> None:
        with self.connection.cursor() as cur:
            query = 'INSERT INTO content.genre_film_work (id, genre_id, film_work_id, created) \
                VALUES (%s, %s, %s, %s) ON CONFLICT (id) DO NOTHING; '
            insert_data = [(g.id, g.genre_id, g.film_work_id, datetime.now())
                           for g in data]
            execute_batch(cur, query, insert_data, page_size=n)
            self.connection.commit()

    def save_all_person_filmworks(self, data: list, n: int = 16) -> None:
        with self.connection.cursor() as cur:
            query = 'INSERT INTO content.person_film_work (id, person_id, film_work_id, role, created) \
                VALUES (%s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING; '
            insert_data = [(p.id, p.person_id, p.film_work_id, p.role,
                            datetime.now()) for p in data]
            execute_batch(cur, query, insert_data, page_size=n)
            self.connection.commit()

