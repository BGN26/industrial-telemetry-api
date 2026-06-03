from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from typing import List

from app.core.database import get_db
from app.models.telemetry import TelemetryData
from app.schemas.telemetry import TelemetryCreate, TelemetryResponse, ReactorAnalytics

router = APIRouter()


@router.post("/telemetry", response_model=TelemetryResponse, status_code=201)
async def ingest_telemetry(data: TelemetryCreate, db: AsyncSession = Depends(get_db)):
# Recibe los datos de la telemetria directos
    new_reading = TelemetryData(
        reactor_id=data.reactor_id,
        temperature=data.temperature,
        pressure=data.pressure
    )
    db.add(new_reading)
    await db.commit()
    await db.refresh(new_reading)
    return new_reading


@router.get("/telemetry/{reactor_id}", response_model=List[TelemetryResponse])
async def get_reactor_history(reactor_id: str, limit: int = 100, db: AsyncSession = Depends(get_db)):
# Info de un reactor concreto
    query = select(TelemetryData).where(TelemetryData.reactor_id == reactor_id).order_by(
        TelemetryData.timestamp.desc()).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()


@router.get("/analytics/{reactor_id}", response_model=ReactorAnalytics)
async def get_reactor_analytics(reactor_id: str, db: AsyncSession = Depends(get_db)):
# Calculo de adiciones en tiempo real
    query = select(
        func.count(TelemetryData.id).label("reading_count"),
        func.avg(TelemetryData.temperature).label("avg_temperature"),
        func.max(TelemetryData.pressure).label("max_pressure")
    ).where(TelemetryData.reactor_id == reactor_id)

    result = await db.execute(query)
    row = result.fetchone()

    # Si el reactor no tiene lecturas, el count sera 0
    if not row or row.reading_count == 0:
        raise HTTPException(status_code=404, detail="No hay datos registrados para este reactor.")

    return ReactorAnalytics(
        reactor_id=reactor_id,
        reading_count=row.reading_count,
        avg_temperature=round(row.avg_temperature, 2),
        max_pressure=round(row.max_pressure, 2)
    )