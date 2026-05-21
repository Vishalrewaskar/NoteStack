"""
Database configuration and session management.

Responsibilities:
- Create database engine
- Manage DB sessions
- Connection handling
- Base ORM setup

Acts as the database entry point.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:root@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)   #SQLAlchemy uses engine to communicate with DB.

SessionLocal = sessionmaker(        # temporary conversation with database
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()   #Every table model will inherit from this.

# Dependency Injection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()