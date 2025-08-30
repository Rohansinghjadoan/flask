from pydantic import BaseModel,Field
class Employee(BaseModel):
    id: int= Field(...,gt=0,title="Employee ID",description="Unique identifier for the employee")
    name: str= Field(...,min_length=3,max_length=30,title="Employee Name",description="Full name of the employee",regex="^[a-zA-Z ]+$")
    department:str=Field(...,min_length=3,max_length=30)
    age: int= Field(...,lt=120)