from dataclasses import dataclass, field
import uuid
import datetime


class DataClassGetter:

    def __init__(self, table):
        self.table = table

    def get_dataclass(self):
        if self.table == 'film_work':
            return Movie
        elif self.table == 'genre':
            return Genre
        elif self.table == 'person':
            return Person
        elif self.table == 'genre_film_work':
            return GenreFilmwork
        elif self.table == 'person_film_work':
            return PersonFilmwork
        else:
            raise Exception("Not existed")


@dataclass
class Movie:
    title: str
    description: str
    creation_date: datetime.date
    created_at: datetime.date
    updated_at: datetime.date
    file_path: str
    type: str
    rating: float = field(default=0.0)
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class Genre:
    name: str
    description: str
    created_at: datetime.date
    updated_at: datetime.date
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class Person:
    full_name: str
    created_at: datetime.date
    updated_at: datetime.date
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class PersonFilmwork:
    role: str
    created_at: datetime.date
    person_id: uuid.UUID
    film_work_id: uuid.UUID
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class GenreFilmwork:
    created_at: datetime.date
    genre_id: uuid.UUID
    film_work_id: uuid.UUID
    id: uuid.UUID = field(default_factory=uuid.uuid4)
