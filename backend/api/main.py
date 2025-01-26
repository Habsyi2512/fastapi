from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
  return {"Hello":"World"}

@app.get("/items/{id}")
def read_item(id:int, q: Union[int, None] = None):
  return {"item_id":id, "q":q}

@app.get("/oi")
def get_oi():
  return {"oi":"oi"}
