from sqlmodel import SQLModel, create_engine, Session
from contextlib import contextmanager

DATABASE_URL = "mysql+pymysql://root:root@localhost/db_todo_fastapi"

engine = create_engine(DATABASE_URL, echo=True)

@contextmanager
def session_scope():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)