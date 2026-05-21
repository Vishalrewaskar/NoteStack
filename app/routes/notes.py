"""
Routes handle API endpoints.

Responsibilities:
- Receive HTTP requests
- Validate request flow
- Call business logic/services
- Return HTTP responses

Routes should stay thin.
Avoid putting heavy business logic here.
"""

from fastapi import APIRouter, HTTPException, Depends   # Depends-> injects database session automatically.
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.note import NoteModel
from app.schemas.note import NoteCreate, NoteUpdate ,Note

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)


@router.get("/", response_model=list[Note])
async def get_notes(db: Session = Depends(get_db)):
    notes = db.query(NoteModel).all()
    return notes


@router.post("/", response_model=Note)
async def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    new_note = NoteModel(
        title = note.title,
        content = note.content
    )
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


@router.get("/{note_id}", response_model=Note)
async def get_note(note_id: int, db : Session = Depends(get_db)):
    note = db.query(NoteModel).filter(NoteModel.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.put("/{note_id}", response_model=Note)
async def update_note(note_id: int,updated_note: NoteUpdate , db : Session = Depends(get_db)):
    note = db.query(NoteModel).filter(NoteModel.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found!")
    if updated_note.title is not None:
        note.title = updated_note.title
    if updated_note.content is not None:
        note.content = updated_note.content
    
    db.commit()
    db.refresh()
    
    return note

@router.delete("/{note_id}")
async def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(NoteModel).filter(NoteModel.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="note not found!")
    db.delete(note)
    db.commit()
    
    return {"message":"Note deleted successfully!"}