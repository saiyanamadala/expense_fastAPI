from sqlalchemy import Column, String, Integer, Float, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer,primary_key=True, index=True)
    amount = Column(Float)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    payment_method = Column(String)
    category = Column(String)
    # user = relationship("User", back_populates='expenses')