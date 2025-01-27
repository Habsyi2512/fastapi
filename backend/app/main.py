from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from .models.user import User
from .database import create_db_and_tables

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
