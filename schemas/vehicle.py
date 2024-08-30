from pydantic import BaseModel, Field
from typing import Optional

class VehicleCreate(BaseModel):
    identification: str = Field(..., max_length=50)
    long: float = Field(..., gt=0)
    width: float = Field(..., gt=0)
    high: float = Field(..., gt=0)
    weight: Optional[float] = None

class VehicleResponse(BaseModel):
    identification: str
    long: float
    width: float
    high: float
    volume: float
    weight: Optional[float]

    class Config:
        orm_mode = True
