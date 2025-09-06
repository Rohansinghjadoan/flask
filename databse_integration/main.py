import models , schemas, crud
from fastapi import  FastAPI
from sqlalchemy.orm import Session
from database import SessionLocal, engine,Base
from typing import List
from fastapi import HTTPException


Base.metadata.create_all(bind=engine) ## create all tables

app=FastAPI()
## Dependency with database session
def get_db():
    db=SessionLocal()
    try:
        yield db ## yield is like return but it will return a generator
    finally:
        db.close()

## endpoints
## 1. Create Employee
@app.post('/employees/', response_model=schemas.EmployeeOut)
def create_employee(employee:schemas.EmployeeCreate, db:Session= next(get_db())):
    return crud.create_employee(db, employee)   
## 2. Get all Employee 
@app.get('/employees/', response_model=List[schemas.EmployeeOut])
def get_employees(db:Session= next(get_db())): ## next(get_db()) will give us the db session
    return crud.get_employees(db)

## 3. Get Employee by id
@app.get('/employees/{emp_id}', response_model=schemas.EmployeeOut)
def get_employee(emp_id:int, db:Session= next(get_db())):
    employee=crud.get_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

## 4. Update Employee by id
@app.put('/employees/{emp_id}', response_model=schemas.EmployeeOut)
def update_employee(emp_id:int, employee:schemas.EmployeeUpdate, db:Session= next(get_db())):
    db_employee=crud.update_employee(db, emp_id, employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee