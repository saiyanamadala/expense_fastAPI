from fastapi import FastAPI
from database import Base, engine
from expense.router import router as expense_router
from user.router import router as user_router

app = FastAPI()

app.include_router(expense_router)
app.include_router(user_router)

Base.metadata.create_all(engine)



