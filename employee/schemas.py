from pydantic import BaseModel
from typing import List,Optional

class employee(BaseModel):
    name : str
    email: str
    phonenumber: int
    country: str
    department: str

    class Config():
        orm_mode = True

class ShowEmployee(BaseModel):
    name : str
    email : str

    class Config():
        orm_mode = True