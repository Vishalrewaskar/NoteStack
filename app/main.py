"""
Application entry point.

Responsibilities:
- Create FastAPI app
- Register routers
- Configure middleware
- Startup/shutdown events

This is where the API starts.
"""

from fastapi import FastAPI
from app.routes.notes import router as notes_router
from app.db.database import engine
from app.models.note import NoteModel


NoteModel.metadata.create_all(bind=engine)

app = FastAPI(title="Notes API")


app.include_router(notes_router)

@app.get("/")
async def root():
    return {"message":"Notes API running"}