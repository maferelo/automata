from fastapi import FastAPI
from fastapi import Request

from app.db import Books
from app.db import BooksReaders
from app.db import database
from app.db import Readers
from app.db import User

app = FastAPI(title="Automata")


@app.get("/")
async def read_root():
    return await User.objects.all()


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    await User.objects.get_or_create(email="test@test.com")


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()


@app.get("/books")
async def get_books():
    return await Books.objects.all()


@app.post("/books")
async def create_book(request: Request):
    data = await request.json()
    book = await Books.objects.create(**data)
    return {"id": book.id}


@app.get("/readers")
async def get_readers():
    return await Readers.objects.all()


@app.post("/readers")
async def create_reader(request: Request):
    data = await request.json()
    book = await Readers.objects.create(**data)
    return {"id": book.id}


@app.post("/read")
async def create_books_readers(request: Request):
    data = await request.json()
    books_readers = await BooksReaders.objects.create(**data)
    return {"id": books_readers.id}
