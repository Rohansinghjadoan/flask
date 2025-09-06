from sqlalchemy import Column, Integer, String
from database import Base

class Employee(Base):
    __tablename__='employees'
    id= Column(Integer,primary_key=True,index=True)## index true means we can search by id and quickly get the data
    name =Column(String, index=True)
    email=Column(String, unique=True, index=True)
