from fastapi import FastAPI

from contextlib import asynccontextmanager
from typing import AsyncIterator

@asynccontextmanager
async def lifespan() -> AsyncIterator[None]:
    yield


def create_application() -> FastAPI:
    _app = FastAPI()
    return _app


app = create_application()


@app.get("/health")
async def health():
    return {"status": "alive"}