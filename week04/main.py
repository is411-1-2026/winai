from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, create_engine, select
from database import engine, init_db
from models import TripDB, TripOut

init_db()
app = FastAPI()

@app.get("/trips/{trip_id}")
def get_tripdb(trip_id: int) -> TripOut:
    with Session(engine) as session:
        statement = select(TripDB).where(TripDB.id == trip_id)
        trip = session.exec(statement).first()

        if trip != None:
            print(trip)
            return trip

    raise HTTPException(
        status_code=404,
        detail='Trip not found'
    )

def insert_tripdb():
    trip_1 = TripDB(name='Sea', destination='Hua Hin', duration=10, price=10000.0, group_size=90)
    trip_2 = TripDB(name='Moutain', destination='Khao Yai', duration=10, price=15000.0, group_size=90)
    trip_3 = TripDB(name='Canel', destination='Amphawa', duration=10, price=8000.0, group_size=90)

    with Session(engine) as session:
        session.add(trip_1)
        session.add(trip_2)
        session.add(trip_3)
        session.commit()
