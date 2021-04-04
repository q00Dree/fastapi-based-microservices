from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

try:
    from app.api.movies import movies
except ModuleNotFoundError:
    from api.movies import movies
    import uvicorn

app = FastAPI()

app.include_router(movies)

if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 8000)