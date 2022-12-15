from employee import models
from database import engine
from employee.database import Base
from employee.router import (
    employee
)
from fastapi import (
    FastAPI
)

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(employee.router)


