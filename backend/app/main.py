from fastapi import FastAPI, status,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from .database import create_db_and_tables, engine
from sqlmodel import Session, select
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

@app.get('/api/users/get-all', response_model=list[User])
def get_users():
    with Session(engine) as session:
        users = session.exec(select(User)).first()
        if not users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")
        return users

@app.post('/api/users/create', status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(user:UserCreate):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user