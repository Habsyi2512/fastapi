from fastapi import Depends
from sqlmodel import Session

def create_user():
    return {"user":"created"}