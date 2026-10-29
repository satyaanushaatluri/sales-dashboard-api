from sqlalchemy import Column, Integer, String, Float
from database import Base

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(String)
    region = Column(String, index=True)
    product = Column(String, index=True)
    amount = Column(Float)

