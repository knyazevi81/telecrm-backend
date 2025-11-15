from fastapi import FastAPI

from contextlib import asynccontextmanager
from typing import AsyncIterator
from app.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    yield


def create_application() -> FastAPI:
    _app = FastAPI(
        lifespan=lifespan,
        title=settings.title
    )
    return _app


app = create_application()


@app.get("/health", tags=["health-check"])
async def health():
    return {"status": "alive"}