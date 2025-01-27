from typing import Union
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from models.user import create_db_and_tables
from contextlib import asynccontextmanager

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
