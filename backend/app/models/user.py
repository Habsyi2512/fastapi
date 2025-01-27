from typing import Optional

from sqlmodel import SQLModel, Field, create_engine

class User(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  name: str
  age: int

  __tablename__ = "users"

class UserCreate(SQLModel):
  name: str
  age: int

