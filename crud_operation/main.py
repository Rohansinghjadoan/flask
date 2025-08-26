from fastapi import FastAPI, HTTPException
from crud_operation.models import Employee

from typing import List

employee_db:List[Employee]=[] 

app=FastAPI()

# 1.read all employees
@app.get("/employees",response_model=List[Employee])
def get_employees():
    return employee_db

# 2.read single employee by id
@app.get("/employees/{emp_id}",response_model=Employee)
def get_employee(emp_id:int):
    for ind,emp in enumerate(employee_db):
        if emp.id==emp_id:
            return employee_db[ind]
    raise HTTPException(status_code=404,detail="Employee not found")

# 3.add new employee
@app.post('/employees',response_model=Employee)
def add_employee(new_emp:Employee):
    for e in employee_db:
        if e.id==new_emp.id:
            raise HTTPException(status_code=400,detail="Employee with this id already exists")
    employee_db.append(new_emp)
    return new_emp
# 4.update existing employee

@app.put('/employees/{emp_id}',response_model=Employee)
def update_employee(emp_id:int,updated_emp:Employee):
    for ind,employee in enumerate(employee_db):
        if employee.id==emp_id:
            employee_db[ind]=updated_emp
            return updated_emp
    raise HTTPException(status_code=404,detail="Employee not found")

# 5.delete employee
@app.delete('/employees/{emp_id}')
def delete_employee(emp_id:int):
    for ind,employee in enumerate(employee_db):
        if employee.id==emp_id:
            del employee_db[ind]
            return {"detail":"Employee deleted successfully"}
    raise HTTPException(status_code=404,detail="Employee not found")
