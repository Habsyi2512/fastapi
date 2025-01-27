from typing import Optional

from sqlmodel import SQLModel, Field, create_engine

class User(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  name: str
  age: int

mysql_url = "mysql://root:root@localhost/db_todo_fastapi"

engine = create_engine(mysql_url, echo=True)

def create_db_and_tables():
  SQLModel.metadata.create_all(engine)
