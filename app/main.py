from fastapi import FastAPI, Request

from app.db import Books, Readers, User, database

app = FastAPI(title="Automata")


@app.get("/")
async def read_root():
    return await User.objects.all()


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    # create a dummy entry
    await User.objects.get_or_create(email="test@test.com")


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()


@app.get("/books")
async def get_books():
    return await Book.objects.all()


@app.post("/books")
async def create_book(request: Request):
    data = await request.json()
    book = await Book.objects.create(**data)
    return {"id": book.id}


@app.post("/readers")
async def create_reader(request: Request):
    data = await request.json()
    book = await Readers.objects.create(**data)
    return {"id": book.id}
