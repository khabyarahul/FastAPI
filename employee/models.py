from sqlalchemy import (
    Column,ForeignKey,Integer,String,text
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from employee.database import Base

class Employee(Base):
    __tablename__ = 'employee'

    emp_id = Column(UUID(as_uuid=True), primary_key=True, default=text('uuid_generate_v4()'))
    name = Column(String)
    email = Column(String)
    phonenumber = Column(Integer)
    country = Column(String)
    department = Column(String)

    