import databases
import ormar
import sqlalchemy

from .config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "users"

    id: int = ormar.Integer(primary_key=True)
    email: str = ormar.String(max_length=128, unique=True, nullable=False)
    active: bool = ormar.Boolean(default=True, nullable=False)


class Readers(ormar.Model):
    class Meta(BaseMeta):
        tablename = "readers"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=128, unique=False, nullable=False)
    lastname: str = ormar.String(max_length=128, unique=False, nullable=True)
    email: str = ormar.String(max_length=128, unique=True, nullable=False)


class Books(ormar.Model):
    class Meta(BaseMeta):
        tablename = "books"

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=128, unique=True, nullable=False)
    author: str = ormar.String(max_length=128, unique=False, nullable=False)


class BooksReaders(ormar.Model):
    class Meta(BaseMeta):
        tablename = "books_readers"
        constraints = [ormar.UniqueColumns("book", "reader")]

    id: int = ormar.Integer(primary_key=True)
    book: Books = ormar.ForeignKey(Books, nullable=False, indexed=True)
    reader: Readers = ormar.ForeignKey(Readers, nullable=False, indexed=True)
