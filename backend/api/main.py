from typing import Union
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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

@app.get("/api")
def read_root():
  return {"Hello":"World"}

@app.get("/api/items/{id}")
def read_item(id:int, q: Union[int, None] = None):
  return {"item_id":id, "q":q}

@app.get("/api/get-profile")
def get_profile():
  return {
    "nama":"Muhammad Habsyi Mubarak",
    "umur":21,
    "pekerjaan":"Mahasiswa",
  }