from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.database import engine, Base
from app.api import endpoints

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # (PTE codigo de apagado)

app = FastAPI(
    title="Industrial Telemetry API",
    description="Microservicio de alta concurrencia para ingesta y analisis de datos de reactores quimicos.",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(endpoints.router, prefix="/api/v1", tags=["Telemetry & Analytics"])