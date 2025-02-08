from typing import Annotated
from fastapi import APIRouter, status
from fastapi.params import Depends
from sqlalchemy.orm import Session
from .service import UserService
from .schema import UserDisplay, User
from database import get_db

router = APIRouter(
    prefix='/user'
)

# db_dependency = Annotated[Session, Depends(get_db())]

# user_service = UserService(db_dependency)

@router.post('/add', response_model=UserDisplay, status_code=status.HTTP_201_CREATED)
def addUser(request: User, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.addUser(request)
