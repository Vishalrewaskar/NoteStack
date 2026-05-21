"""
Schemas define request and response validation.

Used for:
- Data validation
- Serialization
- API contracts
- Automatic documentation

Powered by Pydantic.
"""

from pydantic import BaseModel, Field
from typing import Optional

class NoteCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100, description="Title of the note")
    content: str = Field(min_length=5, max_length=1000, description="Content of the note")


class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


class Note(BaseModel):
    id : int
    title: str
    content: str