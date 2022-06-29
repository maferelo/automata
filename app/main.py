from fastapi import FastAPI

from app.db import User, database

app = FastAPI(title="FastAPI, Docker, and Traefik")


@app.get("/")
async def read_root():
    # return await User.objects.all()
    return [{"id": 1, "email": "test@test.com", "active": True}]


@app.on_event("startup")
async def startup():
    # if not database.is_connected:
    #    await database.connect()
    # create a dummy entry
    # await User.objects.get_or_create(email="test@test.com")
    pass


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()
