from typing import Optional
from typing_extensions import Annotated

from sqlmodel import SQLModel, Field, create_engine

class User(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  name: str
  age: Optional[int]

  __tablename__ = "users"

class UserCreate(SQLModel):
  name: Annotated[str, Field(min_length=3, max_length=55)]
  age: Annotated[Optional[int], Field(default=None, gt=0, le=150)] 

