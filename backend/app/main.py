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
        users = session.exec(select(User)).all()
        if not users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")
        return users

@app.post('/api/users/create', status_code=status.HTTP_201_CREATED, response_model=UserCreate)
def create_user(user_create:UserCreate):
    user = User(**user_create.model_dump())
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
@app.put('/api/users/update/{id}', response_model=UserCreate)
def update_user(id:int, user_create:UserCreate):
    with Session(engine) as session:
        user = session.get(User, id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        user.name = user_create.name
        user.age = user_create.age
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
@app.delete('/api/users/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id:int):
    with Session(engine) as session:
        user = session.get(User, id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        session.delete(user)
        session.commit()
        return