from pydantic import BaseModel
from typing import List, Optional
from user import schema as user_schema


class Expense(BaseModel):
    amount: float
    description: str
    user_id: int
    payment_method: str
    category: str
    user = Optional[user_schema.User]