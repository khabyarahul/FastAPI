from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost/flask_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL,echo = True)

SessionLocal = sessionmaker(bind=engine , autocommit=False, autoflush=False)

Base = declarative_base()

'''
get_db -> Creates Database Session
'''

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()