from sqlalchemy import Column, String, Integer, Float, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String)
    expenses = relationship('Expense', back_populates='user')