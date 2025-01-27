from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from .database import create_db_and_tables, engine
from sqlmodel import Session
from .models.user import User, UserCreate

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_db_and_tables()
    yield
    
app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/api')
def get_api():
    return {"hello":"world"}

@app.post('/api/users/create', status_code=status.HTTP_201_CREATED)
def create_user(user:UserCreate):
    new_user = User(name=user.name, age=user.age)
    with Session(engine) as session:
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
    return {"user":"created"}