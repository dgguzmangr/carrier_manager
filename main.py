from fastapi import FastAPI, HTTPException
from tortoise.contrib.fastapi import register_tortoise
from sqlalchemy.orm import Session
from settings import DATABASES
from schemas.vehicle import VehicleCreate, VehicleResponse
from services.vehicle_service import create_vehicle

app = FastAPI()

# Construir la URL de la base de datos
db_url = f"postgres://{DATABASES['default']['credentials']['user']}:{DATABASES['default']['credentials']['password']}@{DATABASES['default']['credentials']['host']}:{DATABASES['default']['credentials']['port']}/{DATABASES['default']['credentials']['database']}"

# Registrar Tortoise con la URL de la base de datos
register_tortoise(
    app,
    db_url=db_url,
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.post("/vehicles/", response_model=VehicleResponse)
def create_vehicle_endpoint(vehicle_data: VehicleCreate):
    vehicle = create_vehicle(vehicle_data.dict())
    return VehicleResponse(
        identification=vehicle.identification,
        long=vehicle.long,
        width=vehicle.width,
        high=vehicle.high,
        volume=vehicle.volume,
        weight=vehicle.weight
    )
