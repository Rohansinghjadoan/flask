## emplye{ id,name , age .depname}
from pydantic import BaseModel
class Employee(BaseModel):
    id: int
    name: str
    department:str
    age: int