from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# postgresql database URL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost/TodoApplicationDataBase"


# Create engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)  # No extra args needed

# Session local for DB connection
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
