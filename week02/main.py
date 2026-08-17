from fastapi import FastAPI
from pydantic import BaseModel

class Ticket(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

fake_user_db = [
        {'username': 'Focus'},
        {'username': 'Cake'},
        {'username': 'KP'},
        {'username': 'Preme'},
        {'username': 'Benya'},
        {'username': 'Sim'},
    ]

@app.get("/")
def read_root():
    return {"Hello": "Winai"}

@app.get("/users/")
def get_users(skip: int = 0, limit: int = 10):
    return fake_user_db[skip : skip + limit]

@app.get('/user/{user_id}')
def get_user(user_id: int):
    return {'user_id': user_id}

@app.post("/ticket/")
def create_ticket(ticket: Ticket) -> Ticket:
    ticket.tax = ticket.price * .07
    return ticket