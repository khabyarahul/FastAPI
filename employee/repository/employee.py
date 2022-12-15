from sqlalchemy.orm import Session
from fastapi import (
    HTTPException,
    status
)
from FASTAPI.employee import (
    models,
    schemas
)

def get_all(db:Session):
    emp = db.query(models.Employee).all()
    return emp

def create(request:schemas.employee , db:Session):
    new_emp = models.Employee(name = request.name,email = request.email,\
        phonenumber = request.phonenumber,country = request.country,\
            department = request.department,emp_id = 1)
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp

def delete(id:int,db:Session):
    emp = db.query(models.Employee).filter(models.Employee.emp_id == id)
    if not emp.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'{id} not found')
    
    emp.delete(synchronize_session=False)
    db.commit()
    return "Employee Deleted"

def put(id:int,db:Session,request:schemas.employee):
    emp = db.query(models.Employee).filter(models.Employee.emp_id == id)
    if not emp.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'{id} not found')

    emp.update({"name" : request.name,"email" : request.email,\
        "phonenumber" : request.phonenumber,"country" : request.country,\
            "department" : request.department,})
    db.commit()

    return emp

def get_one(id:int,db:Session):
    try:
        emp = db.query(models.Employee).filter(models.Employee.emp_id == id).first()
        if not emp:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} not found")
        return emp
    except Exception as e:
        print(e)
