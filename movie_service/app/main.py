from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

try:
    from app.api.movies import movies
    from app.api.db import metadata, database, engine
    import uvicorn
except ModuleNotFoundError:
    from api.movies import movies
    from api.db import metadata, database, engine
    import uvicorn

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# app.include_router(movies)
app.include_router(movies, prefix='/api/v1/movies', tags=['movies'])

if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 8000)