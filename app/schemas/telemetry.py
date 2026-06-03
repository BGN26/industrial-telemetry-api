from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

# Esquema base
class TelemetryBase(BaseModel):
    reactor_id: str = Field(..., description="ID del reactor quimico (ej. REA-001)", max_length=50)
    temperature: float = Field(..., description="Temperatura del reactor en Celsius")
    pressure: float = Field(..., description="Presion del reactor en bares")

# Esquema de entrada(recibido de los sensores)
class TelemetryCreate(TelemetryBase):
    pass

# Esquema de salida
class TelemetryResponse(TelemetryBase):
    id: int
    timestamp: datetime
    model_config = ConfigDict(from_attributes=True)

# Esquema analitico
class ReactorAnalytics(BaseModel):
    reactor_id: str
    reading_count: int
    avg_temperature: float
    max_pressure: float