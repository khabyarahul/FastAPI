from fastapi import APIRouter , Depends, status

from employee.schemas import ShowEmployee
from employee import schemas
from employee import database
from typing import List
from sqlalchemy.orm import Session
from employee.repository import employee

"""
router = Instance of APIRouter
"""
router = APIRouter(
    prefix= "/emp",
    tags=['employees']
)

# Get data for database
get_db = database.get_db



"""
get = Get perticuler emp from database
"""

@router.get('/{id}' , status_code=status.HTTP_200_OK ,response_model=schemas.ShowEmployee)
def show(id:int , db : Session = Depends(get_db)):
    return employee.get_one(id,db)



"""
get = all emp from database
"""

@router.get('/',response_model=List[schemas.ShowEmployee])
def all(db : Session = Depends(get_db)):
    return employee.get_all(db)



"""
Post = Create New emp
"""

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request :schemas.employee,db : Session = Depends(get_db)):
    return employee.create(request , db)



"""
Delete = Delete emp from database
"""
@router.delete('/{id}' , status_code=status.HTTP_204_NO_CONTENT )
def destroy(id : int , db : Session = Depends (get_db)):
    return employee.delete(id , db)


"""
Put = Update emp from database
"""
@router.put('/{id}' , status_code=status.HTTP_202_ACCEPTED)
def update(id : int, request : schemas.employee ,db : Session = Depends(get_db)):
    return employee.put(id,request,db)



