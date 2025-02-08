from sqlalchemy.orm import Session
from .schema import User
from .model import User

class UserService:

    def __init__(self,db: Session):
        self.db = db


    def addUser(self,request: User):
        new_user = User(name=request.name)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

