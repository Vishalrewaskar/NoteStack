# NoteStack

A scalable backend Notes API built with FastAPI, PostgreSQL, and SQLAlchemy.

NoteStack is a backend-focused project designed to demonstrate modern backend engineering fundamentals including REST API development, database integration, dependency injection, schema validation, and ORM-based architecture.

---

# Features

* RESTful CRUD API
* FastAPI backend architecture
* PostgreSQL database integration
* SQLAlchemy ORM
* Pydantic schema validation
* Modular project structure
* Dependency Injection
* Swagger/OpenAPI documentation
* Error handling with HTTP exceptions
* Production-style backend organization

---

# Tech Stack

| Technology | Purpose                     |
| ---------- | --------------------------- |
| FastAPI    | Backend web framework       |
| PostgreSQL | Relational database         |
| SQLAlchemy | ORM for database operations |
| Pydantic   | Request/response validation |
| Uvicorn    | ASGI server                 |
| Python     | Core programming language   |

---

# Project Structure

```txt
app/
│
├── db/
│   └── database.py
│
├── models/
│   └── note.py
│
├── routes/
│   └── notes.py
│
├── schemas/
│   └── note.py
│
└── main.py
```

---

# Architecture Overview

```txt
Client
   ↓
FastAPI Routes
   ↓
Pydantic Validation
   ↓
SQLAlchemy ORM
   ↓
PostgreSQL Database
```

---

# API Endpoints

| Method | Endpoint           | Description            |
| ------ | ------------------ | ---------------------- |
| GET    | `/`                | Health check           |
| GET    | `/notes/`          | Retrieve all notes     |
| POST   | `/notes/`          | Create a new note      |
| GET    | `/notes/{note_id}` | Retrieve a single note |
| PUT    | `/notes/{note_id}` | Update a note          |
| DELETE | `/notes/{note_id}` | Delete a note          |

---

# Example Request

## Create Note

### Request

```http
POST /notes/
```

```json
{
  "title": "Learn FastAPI",
  "content": "Build scalable backend systems"
}
```

### Response

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "content": "Build scalable backend systems"
}
```

---

# Database Model

```python
class NoteModel(Base):

    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    content = Column(String, nullable=False)
```

---

# Validation

Pydantic schemas are used for:

* Request validation
* Response serialization
* Automatic API documentation
* Type safety
* Data parsing

Example:

```python
class NoteCreate(BaseModel):
    title: str
    content: str
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Vishalrewaskar/NoteStack
cd notestack
```

---

# Create Virtual Environment

Using uv:

```bash
uv venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

# Install Dependencies

```bash
uv add fastapi uvicorn sqlalchemy psycopg2-binary pydantic
```

---

# PostgreSQL Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE notes_db;
```

Update database URL inside:

```txt
app/db/database.py
```

```python
DATABASE_URL = "postgresql://postgres:password@localhost:5432/notes_db"
```

---

# Run Application

```bash
uv run uvicorn app.main:app --reload
```

Server runs at:

```txt
http://127.0.0.1:8000
```

---

# API Documentation

Swagger UI:

```txt
http://127.0.0.1:8000/docs
```

ReDoc:

```txt
http://127.0.0.1:8000/redoc
```

---

# Backend Engineering Concepts Demonstrated

This project demonstrates:

* REST API design
* CRUD operations
* Modular backend architecture
* ORM-based database interaction
* Dependency Injection
* Request/response validation
* PostgreSQL integration
* Error handling
* HTTP status management
* API documentation generation

---

# Future Improvements

Planned scalable backend features:

* JWT Authentication
* User accounts and authorization
* Redis caching
* Rate limiting
* Background task processing
* Async database operations
* AI-powered note summarization
* Semantic search with embeddings
* RAG-based note assistant
* Docker deployment
* CI/CD pipeline
* Monitoring and logging

---

# Learning Objectives

This project was built to strengthen understanding of:

* Backend development fundamentals
* FastAPI architecture
* Database-driven API systems
* Scalable backend patterns
* Production-style API organization
