from pydantic import BaseModel
from typing import List

class User(BaseModel):
    name: str

class UserDisplay(BaseModel):
    id: int
    name: str