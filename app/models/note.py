"""
Models define database tables and ORM mappings.

Responsibilities:
- Table structure
- Database columns
- Relationships
- ORM behavior

Usually built using SQLAlchemy.
"""
from sqlalchemy import Column, Integer, String
from app.db.database import Base

class NoteModel(Base):

    __tablename__ = "notes"         # Actual PostgreSQL table name.

    id = Column(Integer, primary_key=True, index=True)  # Defines DB column.

    title = Column(String, nullable=False)  # nullable=False -> Defines DB column.

    content = Column(String, nullable=False)