from sqlmodel import SQLModel, create_engine, Session
from contextlib import contextmanager
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL, echo=True)

@contextmanager
def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)