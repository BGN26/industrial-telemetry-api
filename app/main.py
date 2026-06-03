from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from app.core.database import engine, Base
from app.api import endpoints
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.core.database import get_db

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

@app.get("/health", tags=["DevOps"])
async def health_check(db: AsyncSession = Depends(get_db)):
    # Endpoint de verificacion del sistema
    try:
        # Hacemos un ping a la base de datos
        await db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        # Si la BD esta caida devolvemos error 503
        raise HTTPException(
            status_code=503,
            detail=f"Database connection failed: {str(e)}"
        )