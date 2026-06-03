from datetime import datetime
from sqlalchemy import String, Float, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class TelemetryData(Base):
    __tablename__ = "telemetry_data"

    # Clave primaria
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    # Identificador del reactor quimico
    reactor_id: Mapped[str] = mapped_column(String(50), index=True)

    # Lecturas de sensores
    temperature: Mapped[float] = mapped_column(Float, comment="Temperatura en grados Celsius")
    pressure: Mapped[float] = mapped_column(Float, comment="Presión en bares")

    # Marca de tiempo generada por la base de datos
    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        index=True
    )