from database import engine
from models.vehicle import Vehicle
from database import Base

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
