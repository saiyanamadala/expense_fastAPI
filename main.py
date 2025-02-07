from fastapi import FastAPI
from expense import model as expense_model
from user import model as user_model
from database import Base, engine
from expense import router as expense_router
from user import router as user_router

app = FastAPI()

app.include_router(expense_router.router)
app.include_router(user_router.router)

Base.metadata.create_all(engine)



