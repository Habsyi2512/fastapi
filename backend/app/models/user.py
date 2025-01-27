from typing import Optional
from typing_extensions import Annotated
from sqlmodel import SQLModel, Field

class UserBase(SQLModel):
  name: Annotated[str, Field(min_length=3, max_length=55)]
  age: Annotated[Optional[int], Field(default=None, gt=0, le=150)] 

class User(UserBase, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  __tablename__ = "users"

class UserCreate(UserBase):
  def response(self):
    return {"message": f"User {self.name} created successfully"}
  

