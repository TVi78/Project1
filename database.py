from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg
import psycopg_binary


DATABASE_URL="postgresql://postgres:7475@127.0.0.1:5432"

engine=create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
Base =declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()