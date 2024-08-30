from sqlalchemy.orm import Session
from models.vehicle import Vehicle
from database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_vehicle(db: Session, vehicle_data: dict):
    vehicle = Vehicle(**vehicle_data)
    db.add(vehicle)
    db.commit()
    db.refresh(vehicle)
    return vehicle
