# We Devided into 4 section

# Section 1 Introduction and setup database, models etc and download

# Introduction and setup database, models etc and download

## Project Overview

### What We're Building

- **ToDo Application** - Create, manage, and track tasks
- **Features**: Create todos, mark complete, set priorities
- **Switch from Books to ToDos** as primary objects

### New Technologies Introduced

- **Full SQL Database** with records and tables
- **Three Database Options**:
  - SQLite (embedded, easy to start)
  - PostgreSQL (production-ready)
  - MySQL (production-ready)
- **Authentication with JWT** (JSON Web Tokens)
- **Authorization with Roles** (admin vs regular users)
- **Password Hashing** for security

### Application Architecture

```
Web Page (Client)
      ↓
  FastAPI Server ← → Database
      ↑               ↑
   JWT Auth      User/ToDo Data

```

---

## Database Fundamentals

### What is a Database?

- **Definition**: Organized collection of structured information/data stored in a computer system
- **Capabilities**:
  - Access data easily
  - Modify data
  - Control and organize data
- **SQL**: Structured Query Language used to modify and write data

### What is Data?

**Example - User Data:**

- Name
- Age
- Email
- Password

### Database Management System (DBMS)

- **Definition**: Software that manages the database
- **Popular SQL Databases**:
  - SQLite
  - MySQL
  - PostgreSQL

### SQL Overview

- **Pronunciation**: "SQL" or "Sequel"
- **Purpose**: Standard language for relational databases
- **Relational Database**: Tables with columns and rows (like Excel sheets)

### CRUD Operations

SQL handles all basic operations:

- **Create** - Insert new data
- **Read** - Select/retrieve data
- **Update** - Modify existing data
- **Delete** - Remove data

---

## Project Setup

### 1. Create Project Structure

```
FastAPI/
└── todoapp/
    ├── __init__.py
    ├── database.py
    ├── models.py
    └── main.py

```

- detail

  ***

  # ⚡ FastAPI Project Setup on Windows

  ## 🔹 Step 1: Project Folder Banao

  ```powershell
  mkdir FastAPI
  cd FastAPI

  ```

  ***

  ## 🔹 Step 2: Virtual Environment Banao

  ```powershell
  python -m venv venv

  ```

  Activate karo (PowerShell):

  ```powershell
  .\venv\Scripts\activate

  ```

  👉 Terminal me `(venv)` likha aayega, matlab environment active hai.

  ***

  ## 🔹 Step 3: Install Packages

  ```powershell
  pip install fastapi uvicorn sqlalchemy

  ```

  (baad me JWT ke liye bhi install karenge, abhi itna kaafi hai)

  ***

  ## 🔹 Step 4: Folder Structure Banao

  ```powershell
  mkdir todoapp
  cd todoapp
  type nul > __init__.py
  type nul > database.py
  type nul > models.py
  type nul > main.py
  cd ..

  ```

  Ab tumhare paas yeh structure hoga:

  ```
  FastAPI/
  │── venv/
  └── todoapp/
      ├── __init__.py
      ├── database.py
      ├── models.py
      └── main.py

  ```

  ***

  # 📂 Har File ka Code

  ## 1️⃣ `__init__.py`

  Ye file khali rakh do, sirf package banane ke liye hai.

  ```python
  # __init__.py
  # Is file ko khali bhi chhod sakte ho

  ```

  ***

  ## 2️⃣ `database.py`

  Database connection setup.

  ```python
  from sqlalchemy import create_engine
  from sqlalchemy.orm import sessionmaker
  from sqlalchemy.ext.declarative import declarative_base

  # SQLite database URL
  SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

  # Engine (SQLite needs special connect_args)
  engine = create_engine(
      SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
  )

  # SessionLocal banane ka tariqa
  SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

  # Base class jisme models banenge
  Base = declarative_base()

  ```

  ***

  ## 3️⃣ `models.py`

  ToDo table define karte hain.

  ```python
  from sqlalchemy import Column, Integer, String, Boolean
  from .database import Base

  class ToDos(Base):
      __tablename__ = "todos"

      id = Column(Integer, primary_key=True, index=True)
      title = Column(String, index=True)
      description = Column(String, index=True)
      priority = Column(Integer)
      complete = Column(Boolean, default=False)

  ```

  ***

  ## 4️⃣ `main.py`

  App banate hain + database table create karte hain.

  ```python
  from fastapi import FastAPI
  from . import models
  from .database import engine

  app = FastAPI()

  # Ye line automatic "todos.db" aur "todos" table bana degi
  models.Base.metadata.create_all(bind=engine)

  @app.get("/")
  def home():
      return {"message": "FastAPI ToDo App ready!"}

  ```

  ***

  # 🔹 Step 5: Server Run Karo

  ```powershell
  cd todoapp
  uvicorn main:app --reload

  ```

  👉 Open browser:

  - [http://127.0.0.1:8000](http://127.0.0.1:8000/) → `"FastAPI ToDo App ready!"`
  - http://127.0.0.1:8000/docs → Swagger UI
    Aur `todoapp` folder me ek **todos.db** file create ho jayegi ✅ (SQLite database).

  ***

### 2. Terminal Navigation

```bash
# Navigate to project directory
cd todoapp

```

### 3. Install Dependencies

```bash
# Install SQLAlchemy (ORM - Object Relational Mapping)
pip install SQLAlchemy

```

**SQLAlchemy**: Connects FastAPI to database and manages database records

---

## Database Configuration (database.py)

### Database URL Setup

```python
# Database location and type
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

```

- Creates SQLite database file in current directory
- File will be named `todos.db`
- Detail

  ```python
  SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

  ```

  ***

  ## 🔹 Agar MySQL use karna ho

  Tumhein **MySQL driver** bhi install karna hoga. SQLAlchemy ke sath commonly yeh use hota hai:

  ```powershell
  pip install pymysql

  ```

  Phir `database.py` me connection string aisi hogi:

  ```python
  SQLALCHEMY_DATABASE_URL = "mysql+pymysql://username:password@localhost:3306/tododb"

  ```

  - `mysql+pymysql` → dialect + driver
  - `username` → tumhara MySQL ka username (zyada tar `root`)
  - `password` → tumhara MySQL ka password
  - `localhost` → agar tum local machine pe run kar rahe ho
  - `3306` → MySQL ka default port
  - `tododb` → tumhara database ka naam (pehle create karna padega)

  ***

  ## 🔹 Agar PostgreSQL use karna ho

  Driver install karo:

  ```powershell
  pip install psycopg2-binary

  ```

  Aur URL aisa hoga:

  ```python
  SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://username:password@localhost:5432/tododb"

  ```

  ***

  👉 Matlab tum `SQLALCHEMY_DATABASE_URL` me `"sqlite:///./todos.db"` ki jagah **apne DB ka URL** likh doge, bas.

  ***

### Engine Creation

```python
from sqlalchemy import create_engine

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

```

- **Engine**: Opens and manages database connections
- **check_same_thread: False**: Allows multiple threads (FastAPI needs this)

### Session Configuration

```python
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

```

- **SessionLocal**: Creates database sessions
- **autocommit/autoflush = False**: Manual control over database transactions

### Base Class Setup

```python
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

```

- **Base**: Foundation for creating database table models

---

## Database Models (models.py)

### ToDo Table Structure

```python
from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class ToDos(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)

```

### Column Explanations

- **id**: Unique identifier (Primary Key)
  - `primary_key=True`: Makes it unique
  - `index=True`: Improves performance
- **title**: Task name (String)
- **description**: Task details (String)
- **priority**: Importance level (Integer)
- **complete**: Done status (Boolean, defaults to False)

### Data Types Used

- **Integer**: Whole numbers
- **String**: Text data
- **Boolean**: True/False values

---

## Application Setup (main.py)

### Basic FastAPI App

```python
from fastapi import FastAPI
import models
from database import engine

app = FastAPI()

# Create database tables automatically
models.Base.metadata.create_all(bind=engine)

```

### How Table Creation Works

1. **models.Base.metadata.create_all()** reads all model classes
2. Creates database file (`todos.db`) if it doesn't exist
3. Creates tables with specified columns
4. Happens automatically when app starts

### Running the Application

```bash
# Start the server
uvicorn main:app --reload

```

- Database file `todos.db` appears in todoapp folder
- Tables created automatically

---

## SQLite Installation & Usage

### Windows Installation Steps

1. **Download**: Go to sqlite.org → Downloads
2. **Get**: "SQLite tools Win32 x86" (command line tools bundle)
3. **Extract**: Unzip downloaded file
4. **Install**: Copy to `C:\sqlite3\`
5. **Path Setup**: Add `C:\sqlite3\` to system PATH environment variable
6. **Test**: Open command prompt, type `sqlite3`

### Basic SQLite Commands

### Connect to Database

```bash
sqlite3 todos.db

```

### View Table Structure

```sql
.schema

```

Shows all tables and their columns

### Change Display Mode

```sql
.mode table    -- Nice table format
.mode column   -- Column format
.mode box      -- Boxed format

```

---

## SQL Commands Reference

### INSERT - Adding Data

```sql
-- Basic syntax
INSERT INTO todos (title, description, priority, complete)
VALUES ('Go to store', 'Pick up eggs', 5, false);

-- Multiple examples
INSERT INTO todos (title, description, priority, complete)
VALUES ('Haircut', 'Need 1mm length', 3, false);

INSERT INTO todos (title, description, priority, complete)
VALUES ('Feed dog', 'Use new food brand', 5, false);

```

### SELECT - Reading Data

```sql
-- Get everything
SELECT * FROM todos;

-- Get specific columns
SELECT title FROM todos;
SELECT title, description FROM todos;
SELECT title, description, priority FROM todos;

-- With conditions (WHERE clause)
SELECT * FROM todos WHERE priority = 5;
SELECT * FROM todos WHERE title = 'Feed dog';
SELECT * FROM todos WHERE id = 2;

```

**WHERE Clause**: Filters records based on conditions

- Most common: Filter by ID (primary key)
- Can filter by any column
- Use single quotes for text values

### UPDATE - Modifying Data

```sql
-- Basic syntax
UPDATE todos
SET complete = true
WHERE id = 5;

-- Update by title (less safe)
UPDATE todos
SET complete = true
WHERE title = 'Learn something new';

```

**Best Practice**: Always update by ID (primary key) because it's unique

### DELETE - Removing Data

```sql
-- Delete specific record (safe)
DELETE FROM todos WHERE id = 5;

-- Delete by condition (risky)
DELETE FROM todos WHERE complete = false;

```

**Warning**: Deleting without ID can remove multiple records

---

## Database Operations in Terminal

### Sample Session

```bash
# Connect to database
sqlite3 todos.db

# View structure
.schema

# Set nice display
.mode table

# Add sample data
INSERT INTO todos (title, description, priority, complete)
VALUES ('Go to store', 'Pick up eggs', 5, false);

INSERT INTO todos (title, description, priority, complete)
VALUES ('Cut lawn', 'Grass getting long', 3, false);

INSERT INTO todos (title, description, priority, complete)
VALUES ('Feed dog', 'He is getting hungry', 5, false);

# View all data
SELECT * FROM todos;

# Delete a record
DELETE FROM todos WHERE id = 4;

# Exit SQLite
.quit

```

### Database Behavior Notes

- **Auto-increment ID**: Database automatically assigns unique IDs
- **ID Reuse**: Deleted IDs can be reused for new records
- **Primary Key**: Always unique, never duplicated

---

## Project Architecture Summary

### File Structure & Purposes

```
todoapp/
├── database.py    # Database connection & configuration
├── models.py      # Table definitions (ToDos class)
├── main.py        # FastAPI app & table creation
└── todos.db       # SQLite database file (auto-created)

```

### Key Concepts

1. **ORM (Object Relational Mapping)**: SQLAlchemy converts Python classes to database tables
2. **Models**: Python classes that represent database tables
3. **Sessions**: Manage database connections and transactions
4. **Engine**: Handles database communication
5. **Base**: Foundation for all model classes

### Development Workflow

1. **Define Models** → Python classes with columns
2. **Configure Database** → Connection settings
3. **Create Tables** → Automatic from models
4. **Manipulate Data** → SQL commands or Python code
5. **Test Changes** → SQLite command line tools

---

## Important Notes

### Pydantic Version Differences

**Pydantic v2 Changes:**

- `.dict()` → `.model_dump()`
- `schema_extra` → `json_schema_extra`
- Optional variables need `= None`: `id: Optional[int] = None`

### Security Best Practices

- **Never store plain text passwords** - always hash them
- **Use primary keys for updates/deletes** - prevents accidents
- **Validate user input** - prevent SQL injection
- **Implement proper authentication** - JWT tokens for security

### Production Considerations

- **SQLite**: Good for development, limited for production
- **PostgreSQL/MySQL**: Better for production with multiple users
- **Database migrations**: Plan for schema changes
- **Backup strategies**: Protect against data loss

# Complete Code

```cpp
# ================================================================
# FastAPI Project 3: ToDo App - Complete Code Collection
# ================================================================

# ================================================================
# 1. PROJECT STRUCTURE
# ================================================================
"""
todoapp/
├── __init__.py
├── database.py
├── models.py
└── main.py
"""

# ================================================================
# 2. database.py - Database Configuration
# ================================================================

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL - creates SQLite database in current directory
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# Create database engine
# connect_args needed for SQLite to allow multiple threads (FastAPI requirement)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Create SessionLocal class - each instance will be a database session
SessionLocal = sessionmaker(
    autocommit=False,    # Manual control over commits
    autoflush=False,     # Manual control over flushes
    bind=engine          # Bind to our engine
)

# Create Base class for our models to inherit from
Base = declarative_base()

# ================================================================
# 3. models.py - Database Table Models
# ================================================================

from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class ToDos(Base):
    """
    ToDos table model
    Represents the structure of todos table in database
    """
    __tablename__ = "todos"

    # Primary key - unique identifier for each todo
    id = Column(Integer, primary_key=True, index=True)

    # Todo title
    title = Column(String)

    # Todo description
    description = Column(String)

    # Priority level (integer)
    priority = Column(Integer)

    # Completion status (defaults to False)
    complete = Column(Boolean, default=False)

# ================================================================
# 4. main.py - FastAPI Application Setup
# ================================================================

from fastapi import FastAPI
import models
from database import engine

# Create FastAPI application instance
app = FastAPI()

# Create all database tables based on models
# This runs when the application starts
models.Base.metadata.create_all(bind=engine)

# ================================================================
# 5. INSTALLATION COMMANDS
# ================================================================
"""
# Navigate to project directory
cd todoapp

# Install SQLAlchemy
pip install SQLAlchemy

# Run the application
uvicorn main:app --reload
"""

# ================================================================
# 6. SQL COMMANDS FOR MANUAL DATABASE MANIPULATION
# ================================================================
"""
-- Connect to database
sqlite3 todos.db

-- View table schema
.schema

-- Set display mode for better viewing
.mode table

-- INSERT COMMANDS - Adding new todos
INSERT INTO todos (title, description, priority, complete)
VALUES ('Go to store', 'Pick up eggs', 5, false);

INSERT INTO todos (title, description, priority, complete)
VALUES ('Haircut', 'Need length of 1 millimeter', 3, false);

INSERT INTO todos (title, description, priority, complete)
VALUES ('Feed the dog', 'Make sure to use new food brand', 5, false);

INSERT INTO todos (title, description, priority, complete)
VALUES ('Water plant', 'Inside and outside plants', 4, false);

INSERT INTO todos (title, description, priority, complete)
VALUES ('Learn something new', 'Learn to program', 5, false);

INSERT INTO todos (title, description, priority, complete)
VALUES ('Shower', 'You have not showered in a few days', 5, false);

-- SELECT COMMANDS - Reading data
-- Get all columns and rows
SELECT * FROM todos;

-- Get specific columns
SELECT title FROM todos;
SELECT description FROM todos;
SELECT title, description FROM todos;
SELECT title, description, priority FROM todos;

-- SELECT with WHERE clause (filtering)
SELECT * FROM todos WHERE priority = 5;
SELECT * FROM todos WHERE title = 'Feed dog';
SELECT * FROM todos WHERE id = 2;

-- UPDATE COMMANDS - Modifying existing data
-- Update by ID (recommended - primary key is unique)
UPDATE todos
SET complete = true
WHERE id = 5;

-- Update by title (less safe - could affect multiple records)
UPDATE todos
SET complete = true
WHERE title = 'Learn something new';

-- DELETE COMMANDS - Removing data
-- Delete by ID (safe - targets specific record)
DELETE FROM todos WHERE id = 5;

-- Delete by condition (risky - could delete multiple records)
DELETE FROM todos WHERE complete = false;

-- Exit SQLite
.quit
"""

# ================================================================
# 7. TERMINAL SESSION EXAMPLE
# ================================================================
"""
# Complete example session in terminal

# 1. Navigate to project
cd todoapp

# 2. Connect to database
sqlite3 todos.db

# 3. Set nice display format
.mode table

# 4. View table structure
.schema

# 5. Add some test data
INSERT INTO todos (title, description, priority, complete)
VALUES ('Go to store', 'Pick up eggs', 5, false);

INSERT INTO todos (title, description, priority, complete)
VALUES ('Cut lawn', 'Grass is getting long', 3, false);

INSERT INTO todos (title, description, priority, complete)
VALUES ('Feed dog', 'He is getting hungry', 5, false);

# 6. View all data
SELECT * FROM todos;

# 7. Add another record
INSERT INTO todos (title, description, priority, complete)
VALUES ('Test element', 'This is a test', 1, false);

# 8. View updated data
SELECT * FROM todos;

# 9. Delete test record
DELETE FROM todos WHERE id = 4;

# 10. Confirm deletion
SELECT * FROM todos;

# 11. Exit
.quit
"""

# ================================================================
# 8. KEY DIFFERENCES FOR PYDANTIC V2 (Future Reference)
# ================================================================
"""
When using Pydantic v2, make these changes:

1. .dict() method becomes .model_dump()
   # Old (v1): data.dict()
   # New (v2): data.model_dump()

2. schema_extra becomes json_schema_extra
   # Old (v1):
   class Config:
       schema_extra = {...}

   # New (v2):
   class Config:
       json_schema_extra = {...}

3. Optional fields need default values
   # Old (v1): id: Optional[int]
   # New (v2): id: Optional[int] = None
"""

# ================================================================
# 9. COMPLETE FILE BREAKDOWN
# ================================================================

# File: todoapp/__init__.py (empty file - makes it a Python package)
# Contents: (empty)

# File: todoapp/database.py
"""
Contains:
- Database URL configuration
- SQLAlchemy engine setup
- SessionLocal for database sessions
- Base class for model inheritance
"""

# File: todoapp/models.py
"""
Contains:
- ToDos class defining table structure
- Column definitions with data types
- Primary key and indexing setup
- Default values for columns
"""

# File: todoapp/main.py
"""
Contains:
- FastAPI application instance
- Import of models and database engine
- Automatic table creation on startup
"""

# ================================================================
# 10. DEVELOPMENT WORKFLOW
# ================================================================
"""
1. Create project structure and files
2. Install SQLAlchemy: pip install SQLAlchemy
3. Write database.py for connection setup
4. Write models.py to define table structure
5. Write main.py to create FastAPI app
6. Run application: uvicorn main:app --reload
7. Database file (todos.db) is created automatically
8. Use SQLite commands to test and manipulate data
9. Build API endpoints (covered in next tutorials)
"""
```

---

---

---

---

---

# Section 2 FastAPI Database Integration with SQLAlchemy - Complete Notes

## Database Setup and Connection

### Key Components

- **SQLAlchemy ORM**: Object Relational Mapper that connects Python code to databases
- **Session**: A connection to the database that handles transactions
- **Dependency Injection**: Running required code before executing main function

### Database Connection Function

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

```

**Important Points:**

- `yield` executes code before sending response
- Code after `yield` runs after response is delivered
- Always close database connections after use for safety

### Dependency Injection Setup

```python
# Create reusable dependency
db_dependency = Annotated[Session, Depends(get_db)]

```

- **`Session`** → tumhara type hai (SQLAlchemy session).
- **`Depends(get_db)`** → FastAPI ko batata hai ke ye value `get_db()` function se aayegi.
- **`Annotated`** → dono cheezon ko ek type hint ke saath combine karta hai.

## CRUD Operations Implementation

### 1. READ All Records (GET)

```python
@app.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(Todos).all()

```

**Process Flow:**

```
Client Request → Open DB Connection → Query All Records → Return Data → Close Connection

```

### 2. READ Single Record by ID (GET)

```python
@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependency,
                    todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail="Todo not found")

```

**Key Features:**

- Path validation: `Path(gt=0)` ensures ID > 0
- `.first()` returns first match for performance
- Returns 404 if record not found

### 3. CREATE New Record (POST)

### Pydantic Request Model

```python
class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool

```

**Field Validations:**

- Title: minimum 3 characters
- Description: 3-100 characters
- Priority: 1-5 (greater than 0, less than 6)
- Complete: boolean (no validation needed)

### Create Endpoint

```python
@app.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency,
                      todo_request: TodoRequest):
    todo_model = Todos(**todo_request.model_dump())
    db.add(todo_model)
    db.commit()

```

**Note:** ID is auto-incremented by database (primary key)

### 4. UPDATE Record (PUT)

```python
@app.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db: db_dependency,
                      todo_id: int = Path(gt=0),
                      todo_request: TodoRequest):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    # Update fields
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()

```

**Critical:** Must update the SAME model retrieved from database, not create new one

### 5. DELETE Record (DELETE)

```python
@app.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency,
                      todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()

```

## Status Codes Used

- **200 OK**: Successful GET request
- **201 Created**: Successful POST request
- **204 No Content**: Successful PUT/DELETE (no response body)
- **404 Not Found**: Record doesn't exist
- **422 Unprocessable Entity**: Validation error

## Database Transaction Flow

```
ASCII Visualization of CRUD Operations:

CREATE:
┌────────┐    Request    ┌─────────┐    Add     ┌──────────┐
│ Client │ ────────────> │ FastAPI │ ────────> │ Database │
└────────┘   with data   └─────────┘   Commit   └──────────┘
                              │
                         Validation
                              ↓
                         Auto-increment ID

READ:
┌────────┐     GET       ┌─────────┐    Query    ┌──────────┐
│ Client │ ────────────> │ FastAPI │ ────────> │ Database │
└────────┘               └─────────┘            └──────────┘
     ↑                        │                       │
     └────────────────────────┴───────────────────────┘
              Return Data

UPDATE:
┌────────┐   PUT + ID    ┌─────────┐   Find     ┌──────────┐
│ Client │ ────────────> │ FastAPI │ ────────> │ Database │
└────────┘   with data   └─────────┘   Update   └──────────┘
                              │         Commit
                         Check exists
                              ↓
                         Modify fields

DELETE:
┌────────┐  DELETE + ID  ┌─────────┐   Find     ┌──────────┐
│ Client │ ────────────> │ FastAPI │ ────────> │ Database │
└────────┘               └─────────┘   Delete   └──────────┘
                              │         Commit
                         Check exists

```

## Important Best Practices

1. **Always validate input data** using Pydantic models
2. **Close database connections** after each use
3. **Use dependency injection** for database sessions
4. **Check if record exists** before update/delete operations
5. **Use appropriate status codes** for different operations
6. **Handle exceptions properly** with meaningful error messages
7. **Use `.first()` for single record queries** (performance optimization)

## Common Pitfalls to Avoid

- ❌ Don't manually set primary key IDs
- ❌ Don't create new model instance for updates
- ❌ Don't forget to commit transactions
- ❌ Don't leave database connections open
- ❌ Don't allow negative or zero IDs in path parameters

## Testing the API

Use `/docs` endpoint to test all operations:

1. Create a todo (POST)
2. Read all todos (GET)
3. Read specific todo by ID (GET)
4. Update a todo (PUT)
5. Delete a todo (DELETE)

```python
from fastapi import FastAPI, Depends, HTTPException, status, Path
from typing import Annotated
from sqlalchemy.orm import Session
from . import models
from .models import Todo

from .database import engine, SessionLocal
from pydantic import BaseModel, Field

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Create reusable dependency
db_dependency = Annotated[Session, Depends(get_db)]

class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    completed: bool

@app.get("/todos", status_code=status.HTTP_200_OK)
def read_todos(db: db_dependency):
    todos = db.query(Todo).all()
    if not todos:
        raise HTTPException(status_code=404, detail="No todos found")
    return todos

@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependency,
                    todo_id: int = Path(gt=0)):
    todo_model = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail="Todo not found")

@app.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency,
                      todo_request: TodoRequest):
    todo_model = Todo(**todo_request.model_dump())
    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)
    return todo_model



@app.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db: db_dependency, todo_request: TodoRequest,
                      todo_id: int = Path(gt=0)):
    todo_model = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    # Update fields
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.completed = todo_request.completed

    db.add(todo_model)
    db.commit()
    return {"message": "Todo updated successfully "}

@app.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency,
                      todo_id: int = Path(gt=0)):
    todo_model = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(todo_model)
    db.commit()
    raise HTTPException(status_code=201, detail="Todo Deleted")
```

---

---

---

---

---

# Section 3 authentication and authorization

### Topic: Authentication and Authorization Setup with Routing

[To the point FastAPI Authentication & Authorization ](https://www.notion.so/To-the-point-FastAPI-Authentication-Authorization-270ba39463a080c0bb68db614043f59e?pvs=21)

### Outline

1. Create auth.py file for authentication logic
2. Problem with separate FastAPI instances
3. Implement FastAPI Router solution
4. Create routers package and organize files
5. Update project structure in PyCharm
6. Clean up main.py with router imports

---

### 1. Create auth.py file for authentication logic

- Right click TODO app folder
- Select "New Python file"
- Name it "auth.py"
- Add FastAPI setup:

**File: auth.py**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_user():
    return {"user": "authenticated"}

```

- Test with terminal command:

```bash
uvicorn main:app --reload

```

- Problem: auth.py endpoint doesn't appear in main app

### 2. Problem with separate FastAPI instances

- auth.py creates separate FastAPI application
- Running auth.py requires different command:

```bash
uvicorn auth:app --reload

```

- This hides main.py endpoints
- Need solution to run both on same port

### 3. Implement FastAPI Router solution

- Router allows main file to be root of application
- Different routes lead to different FastAPI files
- Change auth.py to use APIRouter:

**File: auth.py**

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_user():
    return {"user": "authenticated"}

```

- Update main.py to include router:

**File: main.py**

```python
# Add after models.Base.metadata.create_all line
from routers import auth

app.include_router(auth.router)

```

### 4. Create routers package and organize files

- Right click TODO app
- Select "New Python package"
- Name it "routers"
- Move auth.py into routers package
- Select "Yes, refactor" when prompted
- Test with:

```bash
uvicorn main:app --reload

```

- Both auth and todos endpoints now appear together

### 5. Update project structure in PyCharm

- File → Open new project
- Navigate to fast API application → todo app
- Open todo app as new project
- Select "This window"
- This makes todo app the parent location instead of fast API directory

### 6. Clean up main.py with router imports

- Create new todos.py router file:

**File: routers/todos.py**

```python
from fastapi import APIRouter

router = APIRouter()

# Copy all existing API endpoints from main.py
# Change 'app' to 'router' in all decorators

```

- Update main.py:

**File: main.py**

```python
from fastapi import FastAPI
from database import engine
import models
from routers import auth, todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)

```

- Remove all API endpoints from main.py
- Remove unneeded imports
- Test with:

```bash
uvicorn main:app --reload

```

---

### Topic: One-to-Many Relationships in Database

### Outline

1. Understanding one-to-many relationships
2. Database table structure explanation
3. Adding foreign key to todos table
4. How foreign keys work with primary keys

---

### 1. Understanding one-to-many relationships

- Single user can have multiple todos
- A todo cannot have multiple users
- Example: One user has multiple todos (garbage, haircut, shower, etc.)
- Multiple users can exist, each with their own group of todos

### 2. Database table structure explanation

- Two separate tables: users and todos
- Users table: ID (primary key), email, username, first_name, last_name, hashed_password, is_active
- Todos table: ID (primary key), todo description, priority, complete
- Need to connect user to many different todo records

### 3. Adding foreign key to todos table

- Add new field called "owner" to todos table
- Owner field has FK (foreign key) notation
- Foreign key holds primary key of user record
- New todos table structure: ID (primary key), title, description, priority, complete, owner (foreign key)

### 4. How foreign keys work with primary keys

- Foreign key references primary key of another table
- Example data:
  - User 1: email="codingwithrobie", first_name="Eric"
  - User 2: example user with fake data
- Todos with owner column showing 1s and 2s
- All todos with foreign key "1" belong to coding with robie
- All todos with foreign key "2" belong to example user
- SQL query example: `SELECT * FROM todos WHERE owner = 1`

---

### Topic: Foreign Keys Explanation

### Outline

1. Definition of foreign key
2. How foreign keys link tables
3. SQL examples with foreign keys
4. Using user ID in API requests

---

### 1. Definition of foreign key

- Foreign key referenced by FK
- Column in relational database table
- Provides link between two separate tables
- References primary key of another table
- Most relational databases need foreign keys to link tables

### 2. How foreign keys link tables

- Linking todos to single user
- One user to many different todos relationship
- Example: `SELECT * FROM todos` shows todos table with owner column (foreign key)
- Example: `SELECT * FROM users` shows users table without foreign key column
- Only reference todos back to user due to one-to-many relationship

### 3. SQL examples with foreign keys

- Query todos for specific user: `SELECT * FROM todos WHERE owner = 1`
- Returns all todos where owner equals 1
- Query for different user: `SELECT * FROM todos WHERE owner = 2`
- Returns all todos where owner equals 2

### 4. Using user ID in API requests

- Each API request will have user ID attached
- Future videos will extract user ID from JWT (JSON Web Token)
- Can use ID to find user's todos
- Skip querying users table since we have user ID from request

---

### Topic: Database Enhancement with Users Table

### Outline

1. Rename database file
2. Delete old database
3. Create Users class in models
4. Add user table columns
5. Update todos table with foreign key
6. Test new database creation

---

### 1. Rename database file

- Change database name in database.py
- Current name "todos.db" is confusing
- Update to "todosapp":

**File: database.py**

```python
# Change SQLite database name
SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db"

```

### 2. Delete old database

- Right click todos.db file
- Select delete
- Check all options and click OK
- SQLAlchemy will create new database when we run application

### 3. Create Users class in models

- Add above todos class:

**File: models.py**

```python
class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)

```

### 4. Add user table columns

- ID: primary key, indexable
- Email: unique string
- Username: unique string
- First name: string
- Last name: string
- Hashed password: encrypted password string
- Is active: boolean, defaults to true
- Role: string for admin/user roles

### 5. Update todos table with foreign key

- Add to bottom of Todos class:

**File: models.py**

```python
# Add to Todos class
owner_id = Column(Integer, ForeignKey("users.id"))

```

- Import ForeignKey:

```python
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

```

### 6. Test new database creation

- Run application:

```bash
uvicorn main:app --reload

```

- Creates new todosapp.db with both users and todos tables
- Previous todos data is gone (deleted old database)
- Enhanced todos table now has owner_id foreign key

---

**Next Topic Preview:** The instructor mentioned implementing authentication and authorization within the application, and using JWT (JSON Web Tokens) for user identification in future videos.

# Code FastAPI Project Structure and Complete Code

## Project Structure

```
todoapp/
├── main.py
├── database.py
├── models.py
└── routers/
    ├── __init__.py
    ├── auth.py
    └── todos.py

```

## Complete Code Files

### File: main.py

```python
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import todos, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todos.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

### File: database.py

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLite database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db"

# Create engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Session local for DB connection
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

```

### File: models.py

```python
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from todoapp.database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    complete = Column(Boolean, default=False)
    priority = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.id"))

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)
```

### File: routers/**init**.py

```python
# Empty file - makes routers a Python package

```

### File: routers/auth.py

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_user():
    return {"user": "authenticated"}
```

### File: routers/todos.py

```python
from fastapi import APIRouter, Depends, HTTPException, status, Path
from typing import Annotated
from sqlalchemy.orm import Session
from todoapp.models import Todo
from todoapp import models  # Add this import
from ..database import engine, SessionLocal
from pydantic import BaseModel, Field

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Create reusable dependency
db_dependency = Annotated[Session, Depends(get_db)]

class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    completed: bool
    priority: int = Field(gt=0, le=5)  # Add priority field

@router.get("/todos", status_code=status.HTTP_200_OK)
def read_todos(db: db_dependency):
    todos = db.query(Todo).all()
    if not todos:
        raise HTTPException(status_code=404, detail="No todos found")
    return todos

@router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail="Todo not found")

@router.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: TodoRequest):
    todo_model = Todo(
        title=todo_request.title,
        description=todo_request.description,
        complete=todo_request.completed,  # Note: mapping completed -> complete
        priority=todo_request.priority,
        owner_id=1  # You'll want to get this from authentication later
    )
    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)
    return todo_model

@router.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db: db_dependency, todo_request: TodoRequest, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    # Update fields (note: mapping completed -> complete)
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.complete = todo_request.completed  # completed -> complete
    todo_model.priority = todo_request.priority

    db.add(todo_model)
    db.commit()

@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(todo_model)
    db.commit()
```

## Key Changes Made

### 1. Project Organization

- Created `routers/` package for better code organization
- Separated authentication logic (`auth.py`) from todos logic (`todos.py`)
- Clean `main.py` that only handles app setup and router inclusion

### 2. Database Enhancements

- **Renamed database**: `todos.db` → `todosapp.db`
- **Added Users table** with fields:
  - `id` (primary key, indexed)
  - `email` (unique)
  - `username` (unique)
  - `first_name`, `last_name`
  - `hashed_password` (for secure password storage)
  - `is_active` (defaults to True)
  - `role` (for admin/user permissions)

### 3. Foreign Key Relationship

- Added `owner_id` to Todos table
- Foreign key references `users.id`
- Enables one-to-many relationship (one user → many todos)

### 4. Router Implementation

- Used `APIRouter` instead of multiple `FastAPI()` instances
- All endpoints accessible on same port
- Better scalability and maintainability

## How to Run

```bash
# Make sure you're in the todoapp directory
uvicorn todoapp.main:app --reload

```

## Database Structure

The application creates two tables:

**users table:**

- id (PK, indexed)
- email (unique)
- username (unique)
- first_name
- last_name
- hashed_password
- is_active (default: True)
- role

**todos table:**

- id (PK, indexed)
- title
- description
- priority
- complete (default: False)
- owner_id (FK → users.id)

## Notes

- The old `todos.db` file is deleted, so previous data is lost
- Authentication logic is prepared but not fully implemented yet
- `owner_id` in todos will be populated when user authentication is added
- The project structure supports future authentication and authorization features

---

---

---

---

### Topic: Creating User Registration with Pydantic Validation

### Outline

1. Change auth endpoint to POST and create Pydantic validation class
2. Create user model and handle password field differences
3. Test user creation endpoint

---

### 1. Change auth endpoint to POST and create Pydantic validation class

- Change router.get to router.post
- Change function name from get_user to create_user
- Create Pydantic class above the endpoint:

**File: routers/auth.py**

```python
from pydantic import BaseModel

class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str

```

### 2. Create user model and handle password field differences

- Import Users model:

```python
from models import Users

```

- Add parameter to endpoint function:

```python
@router.post("/auth")
async def create_user(create_user_request: CreateUserRequest):

```

- Create user model manually (cannot use dictionary method because password vs hashed_password mismatch):

```python
create_user_model = Users(
    email=create_user_request.email,
    username=create_user_request.username,
    first_name=create_user_request.first_name,
    last_name=create_user_request.last_name,
    role=create_user_request.role,
    hashed_password=create_user_request.password,  # temporarily plain text
    is_active=True
)

return create_user_model

```

### 3. Test user creation endpoint

- Run application:

```bash
uvicorn main:app --reload

```

- Test with sample data:
  - Username: coding with ruby
  - Email: codingwithrruby@gmail.com
  - First name: Eric
  - Last name: Roby
  - Password: test1234
  - Role: admin
- Returns status code 200 with user model information

---

### Topic 2: Password Hashing with Bcrypt

### Outline

1. Install required dependencies
2. Set up bcrypt context
3. Hash password in user creation
4. Test password hashing

---

### 1. Install required dependencies

- Stop terminal with Ctrl+C
- Install dependencies:

```bash
pip install passlib
pip install bcrypt==4.0.1

```

- Important: Must use bcrypt==4.0.1 specifically

### 2. Set up bcrypt context

- Import at top of file:

```python
from passlib.context import CryptContext

```

- Create bcrypt context below router:

```python
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

```

### 3. Hash password in user creation

- Replace plain text password assignment:

```python
hashed_password = bcrypt_context.hash(create_user_request.password)

```

- Update user model creation:

```python
create_user_model = Users(
    email=create_user_request.email,
    username=create_user_request.username,
    first_name=create_user_request.first_name,
    last_name=create_user_request.last_name,
    role=create_user_request.role,
    hashed_password=hashed_password,
    is_active=True
)

```

### 4. Test password hashing

- Run application:

```bash
uvicorn main:app --reload

```

- Test with same data as before
- Password "test1234" now returns as long hashed string
- Hashed password no longer resembles original text

---

### Topic 3: Saving Users to Database

### Outline

1. Add database dependency and imports
2. Update endpoint with database operations
3. Test user creation and database storage

---

### 1. Add database dependency and imports

- Copy database dependency from todos.py:

```python
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends
from database import SessionLocal

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

```

- Add status code import:

```python
from starlette import status

```

### 2. Update endpoint with database operations

- Update endpoint signature:

```python
@router.post("/auth", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):

```

- Replace return statement with database operations:

```python
db.add(create_user_model)
db.commit()

```

### 3. Test user creation and database storage

- Run application:

```bash
uvicorn main:app --reload

```

- Test user creation - returns 201 status code with null response body
- Verify in database:

```bash
sqlite3 todosapp.db
SELECT * FROM users;

```

- User record appears with hashed password and is_active=1 (true)

---

### Topic 4: User Authentication Setup

### Outline

1. Create login endpoint with OAuth2 form
2. Install python-multipart dependency
3. Create authenticate_user function
4. Test authentication process

---

### 1. Create login endpoint with OAuth2 form

- Install dependency:

```bash
pip install python-multipart

```

- detail
  `python-multipart` FastAPI ke andar **file uploads aur form-data handle karne** ke liye use hota hai.

  ### Samajhne ka tariqa:

  HTTP requests do common formats me data bhejti hain:

  1. **application/json** → Normal APIs me JSON data (FastAPI isko by default handle karta hai).
  2. **multipart/form-data** → Jab hum **form data ya files (images, pdf, etc.)** upload karte hain, to data multipart form me aata hai.
     FastAPI ko is `multipart/form-data` ko parse karna nahi aata by default, is liye humein `python-multipart` library install karni padti hai.

  ***

  ### Example:

  ```python
  from fastapi import FastAPI, File, UploadFile, Form

  app = FastAPI()

  @app.post("/upload/")
  async def upload_file(
      username: str = Form(...),       # form field
      file: UploadFile = File(...)     # file field
  ):
      return {"filename": file.filename, "username": username}

  ```

  👉 Agar tum `pip install python-multipart` nahi karte to upar wala code error dega:
  `RuntimeError: Form data requires "python-multipart" to be installed.`

  ***

  🔑 **Simple words me:**
  `python-multipart` = **FastAPI ko sikhaata hai ke "form-data aur file uploads" ko kaise samjhna hai.**

  ***

- Import OAuth2 form:

```python
from fastapi.security import OAuth2PasswordRequestForm

```

- detail
  `OAuth2PasswordRequestForm` FastAPI ka ek **built-in helper class** hai jo mainly **login endpoints** ke liye use hota hai.
  👉 Ye kya karta hai?

  - Jab client login form bhejta hai (`username` aur `password`) `application/x-www-form-urlencoded` format me, to ye class automatically usko parse karke tumhe Python object de deti hai.

  ***

  ### Example

  ```python
  from fastapi import FastAPI, Depends
  from fastapi.security import OAuth2PasswordRequestForm

  app = FastAPI()

  @app.post("/login")
  async def login(form_data: OAuth2PasswordRequestForm = Depends()):
      # form_data object me values hoti hain
      username = form_data.username
      password = form_data.password
      return {"username": username, "password": password}

  ```

  ***

  ### Request Example (Postman ya curl se bhejna hoga):

  ```
  POST http://127.0.0.1:8000/login
  Content-Type: application/x-www-form-urlencoded

  username=hamza&password=12345

  ```

  ***

  ### Output

  ```json
  {
    "username": "hamza",
    "password": "12345"
  }
  ```

  ***

  ⚡ Important: Ye chalane ke liye tumhe `python-multipart` package install karna zaroori hai, warna FastAPI form-data parse nahi kar paayega.

  ***

- Create login endpoint:

```python
@router.post("/token")
async def login_for_access_token():
    return "token"

```

### 2. Add form data and database dependency

- Update endpoint with dependencies:

```python
@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: db_dependency
):
    return form_data.username

```

### 3. Create authenticate_user function

- Create function above endpoint:

```python
def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return True

```

### 4. Test authentication process

- Update endpoint to use authentication:

```python
user = authenticate_user(form_data.username, form_data.password, db)
if not user:
    return "Failed Authentication"
return "Successful Authentication"

```

- Test cases:
  - Wrong username/password: returns "Failed Authentication"
  - Correct username (codingwithruby) + wrong password: returns "Failed Authentication"
  - Correct username + correct password (test1234): returns "Successful Authentication"

---

### Topic 5: JWT (JSON Web Token) Theory

### Outline

1. What is a JSON Web Token
2. JWT Structure and Components
3. JWT Security and Usage
4. Practical Use Cases

---

### 1. What is a JSON Web Token

- JWT stands for JSON Web Token
- Self-contained way to securely transmit data between parties using JSON object
- Can be trusted because each JWT can be digitally signed
- Server can detect if JSON object has been changed by client
- Authorization method (not authentication method)
- Allows client and server to maintain relationship without logging in each request

### 2. JWT Structure and Components

- JWT has three parts separated by dots: `header.payload.signature`
- **JWT Header**: First part containing algorithm for signing and token type, encoded using Base64
- **JWT Payload**: Second part containing actual user data and claims
  - Three types of claims: registered, public, private
  - Key registered claims:
    - `iss` (issuer): identifies who issued the JWT
    - `sub` (subject): statements about the subject, must be unique
    - `exp` (expiration): when JWT expires
- **JWT Signature**: Third part created by hashing encoded header + encoded payload + secret

### 3. JWT Security and Usage

- Example payload data: subject, name, given_name, family_name, email, admin status
- Secret key stored on server (client cannot access)
- Sent in authorization header using bearer schema
- Never send sensitive data to client
- JWT safe as long as client doesn't discover secret key
- Server can immediately identify altered data

### 4. Practical Use Cases

- Multiple applications sharing same secret key
- Example: Cryptocurrency trading app and digital wallet app
- User signs in once, can access both applications seamlessly
- Popular in microservices architecture
- APIs can decode tokens without implementing authentication
- Visit https://jwt.io to encode/decode JWT tokens

---

**Next Topic Preview:** The instructor mentioned implementing JWT token creation and validation in the FastAPI application.

# Code Complete FastAPI Authentication Project Structure and Code

## Project Structure

```
todoapp/
├── main.py
├── database.py
├── models.py
└── routers/
    ├── __init__.py
    ├── auth.py
    └── todos.py

```

## Database File Created

- `todosapp.db` (SQLite database with users and todos tables)

## Complete Code Files

### File: main.py

```python
from fastapi import FastAPI
from database import engine
import models
from routers import auth, todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)

```

### File: database.py

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

```

### File: models.py

```python
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)

class Todos(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

```

### File: routers/**init**.py

```python
# Empty file - makes routers a Python package

```

### File: routers/auth.py

```python
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from database import SessionLocal
from models import Users
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

# Bcrypt context for password hashing
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Database dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

# Pydantic model for user creation
class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str

# Authentication function
def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return True

# User registration endpoint
@router.post("/auth", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True
    )

    db.add(create_user_model)
    db.commit()

# Login endpoint
@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: db_dependency
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        return "Failed Authentication"
    return "Successful Authentication"

```

### File: routers/todos.py

```python
from fastapi import APIRouter, Depends, HTTPException, Path
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Todos
from typing import Annotated

router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool

@router.get("/")
async def read_all(db: db_dependency):
    return db.query(Todos).all()

@router.get("/todo/{todo_id}")
async def read_todo(todo_id: int = Path(gt=0), db: db_dependency):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail="Todo not found")

@router.post("/")
async def create_todo(todo_request: TodoRequest, db: db_dependency):
    todo_model = Todos()
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete
    # owner_id will be set later when authentication is implemented

    db.add(todo_model)
    db.commit()

@router.put("/{todo_id}")
async def update_todo(todo_id: int, todo_request: TodoRequest, db: db_dependency):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()

    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()

@router.delete("/{todo_id}")
async def delete_todo(todo_id: int, db: db_dependency):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()

    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()

```

## Required Dependencies

### Install Commands

```bash
pip install passlib
pip install bcrypt==4.0.1
pip install python-multipart

```

## How to Run

```bash
uvicorn main:app --reload

```

## Database Operations

### Check users table

```bash
sqlite3 todosapp.db
SELECT * FROM users;

```

## API Endpoints Available

### Authentication Endpoints

- **POST /auth** - Create new user (registration)
- **POST /token** - User login (authentication)

### Todo Endpoints

- **GET /** - Get all todos
- **GET /todo/{todo_id}** - Get specific todo
- **POST /** - Create new todo
- **PUT /{todo_id}** - Update todo
- **DELETE /{todo_id}** - Delete todo

## Key Features Implemented

### User Registration

- Pydantic validation for user input
- Bcrypt password hashing
- User data stored in database with hashed passwords
- Returns 201 status code on successful creation

### User Authentication

- OAuth2PasswordRequestForm for secure login
- Username/password validation against database
- Bcrypt password verification
- Returns success/failure messages

### Database Structure

- **users table**: id, email, username, first_name, last_name, hashed_password, is_active, role
- **todos table**: id, title, description, priority, complete, owner_id (foreign key)
- One-to-many relationship between users and todos

## Security Features

- Passwords are hashed using bcrypt (never stored as plain text)
- OAuth2PasswordRequestForm for secure authentication
- Database foreign key relationships
- Input validation with Pydantic models

## Current Limitations

- JWT token generation not yet implemented
- Authentication returns simple text messages instead of tokens
- Todo endpoints don't yet use user authentication
- No authorization checks on protected endpoints

The project is set up for the next phase where JWT tokens will be implemented for proper authentication and authorization.

---

---

---

---

### Topic: Creating JWT Tokens for Authentication

### Outline

1. Install JWT library and setup secret/algorithm
2. Create access token function
3. Update login endpoint to return JWT
4. Add Token response model
5. Test JWT creation

---

### 1. Install JWT library and setup secret/algorithm

- Install dependency:

```bash
pip install "python-jose[cryptography]"

```

- Add imports and setup:
  **File: routers/auth.py**

```python
from jose import jwt
from datetime import datetime, timedelta, timezone

```

- Add secret key and algorithm below router:

```python
# Generate secret with: openssl rand -hex 32
SECRET_KEY = "your-long-secret-string-here"
ALGORITHM = "HS256"

```

### 2. Create access token function

- Add function below authenticate_user:

```python
def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id}
    expire = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

```

### 3. Update login endpoint to return JWT

- Fix authenticate_user function to return user object:

```python
def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user  # Return user object, not True

```

- Update login endpoint:

```python
@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: db_dependency
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        return "Failed Authentication"

    token = create_access_token(user.username, user.id, timedelta(minutes=20))
    return token

```

### 4. Add Token response model

- Create Token class below CreateUserRequest:

```python
class Token(BaseModel):
    access_token: str
    token_type: str

```

- Update login endpoint with response model:

```python
@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: db_dependency
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        return "Failed Authentication"

    token = create_access_token(user.username, user.id, timedelta(minutes=20))
    return {'access_token': token, 'token_type': 'bearer'}

```

### 5. Test JWT creation

- Run application:

```bash
uvicorn main:app --reload

```

- Test login with correct credentials
- Copy token and verify at jwt.io
- Token contains: algorithm HS256, sub (username), id (user_id), exp (expiration)
  ***

### Topic: JWT Token Decoding and Validation

### Outline

1. Import OAuth2PasswordBearer
2. Create OAuth2 bearer dependency
3. Create get_current_user function
4. Add error handling for invalid tokens

---

### 1. Import OAuth2PasswordBearer

- Add import:

```python
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

```

### 2. Create OAuth2 bearer dependency

- Add below bcrypt_context:

```python
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")

```

### 3. Create get_current_user function

- Add imports for error handling:

```python
from fastapi import APIRouter, Depends, HTTPException
from jose import jwt, JWTError

```

- Create function below create_access_token:

```python
async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Could not validate credentials'
            )
        return {'username': username, 'id': user_id}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials'
        )

```

### 4. Add error handling for invalid tokens

- Update login endpoint error handling:

```python
@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: db_dependency
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials'
        )

    token = create_access_token(user.username, user.id, timedelta(minutes=20))
    return {'access_token': token, 'token_type': 'bearer'}

```

---

### Topic: API Organization with Prefixes and Tags

### Outline

1. Add prefix and tags to auth router
2. Update endpoint paths
3. Update OAuth2 bearer token URL
4. Test organized API structure

---

### 1. Add prefix and tags to auth router

- Update router creation:

```python
router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

```

### 2. Update endpoint paths

- Remove '/auth' from create user endpoint:

```python
@router.post("", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    # ... existing code

```

- Keep token endpoint as is (will become /auth/token):

```python
@router.post("/token", response_model=Token)

```

### 3. Update OAuth2 bearer token URL

- Update tokenUrl to match new prefix:

```python
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

```

### 4. Test organized API structure

- Run application:

```bash
uvicorn main:app --reload

```

- Verify endpoints are grouped under "auth" tag
- Create user endpoint: POST /auth
- Login endpoint: POST /auth/token

---

**Next Topic Preview:** The instructor mentioned implementing authorization in todo endpoints to validate that users have successfully logged in before accessing specific API endpoints.

---

## Complete Code and File Structure

### Project Structure

```
todoapp/
├── main.py
├── database.py
├── models.py
└── routers/
    ├── __init__.py
    ├── auth.py
    └── todos.py

```

### File: routers/auth.py (Complete Updated Code)

```python
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from database import SessionLocal
from models import Users
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

# Generate with: openssl rand -hex 32
SECRET_KEY = "197b2c37c391bed93fe80344fe73b806947a65e36206e05a1a23c2fa12702fe3"
ALGORITHM = "HS256"

# Bcrypt context for password hashing
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 bearer for token validation
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

# Database dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

# Pydantic models
class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str

class Token(BaseModel):
    access_token: str
    token_type: str

# Authentication functions
def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id}
    expire = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Could not validate credentials'
            )
        return {'username': username, 'id': user_id}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials'
        )

# API endpoints
@router.post("", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True
    )

    db.add(create_user_model)
    db.commit()

@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: db_dependency
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials'
        )

    token = create_access_token(user.username, user.id, timedelta(minutes=20))
    return {'access_token': token, 'token_type': 'bearer'}

```

### Required Dependencies

```bash
pip install passlib
pip install bcrypt==4.0.1
pip install python-multipart
pip install "python-jose[cryptography]"

```

### Generate Secret Key

```bash
openssl rand -hex 32

```

### Key Features Added

1. **JWT Token Generation**: Creates secure tokens with user info and expiration
2. **JWT Token Validation**: Decodes and validates tokens for authentication
3. **OAuth2 Bearer Token**: Standard OAuth2 implementation for API security
4. **API Organization**: Grouped auth endpoints with prefix and tags
5. **Error Handling**: Proper HTTP exceptions for authentication failures
6. **Token Expiration**: 20-minute token expiration for security

### API Endpoints

- **POST /auth** - User registration
- **POST /auth/token** - User login (returns JWT token)

### Next Steps

---

---

---

---

# Secton 4 FastAPI Authentication and User Management - Course Notes

## Topic: Adding Authentication to TODO Endpoints

### Outline

1. Import get_current_user function
2. Create user dependency
3. Add authentication to create TODO
4. Add authentication to read all TODOs
5. Add authentication to read TODO by ID
6. Add authentication to update TODO
7. Add authentication to delete TODO
8. Create admin router with special permissions
9. Create users router for profile and password change

---

### 1. Import get_current_user function

**File: todos.py**

- Add import at top of file:

```python
from .auth import get_current_user

```

### 2. Create user dependency

**File: todos.py**

- Add dependency after imports:

```python
user_dependency = Annotated[dict, Depends(get_current_user)]

```

### 3. Add authentication to create TODO

**File: todos.py**

- Update create TODO function:

```python
@router.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(user: user_dependency,
                     todo_request: TodoRequest,
                     db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")

    todo_model = Todos(**todo_request.dict(), owner_id=user.get('id'))
    db.add(todo_model)
    db.commit()



    # I think below is the correct version
@router.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(user: user_dependency,
                     todo_request: TodoRequest,
                     db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")

    todo_model = Todo(
        title=todo_request.title,
        description=todo_request.description,
        complete=todo_request.completed,  # Note: mapping completed -> complete
        priority=todo_request.priority,
        owner_id=user.get('id')  # You'll want to get this from authentication later
    )
    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)
    return todo_model
```

- Run application:

```bash
uvicorn main:app --reload

```

- Test in browser with Swagger UI
- Click lock icon to authorize with username and password
- Execute create TODO endpoint

### 4. Add authentication to read all TODOs

**File: todos.py**

- Update read all function:

```python
@router.get("/")
async def read_all(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")

    return db.query(Todos).filter(Todos.owner_id == user.get('id')).all()

```

### 5. Add authentication to read TODO by ID

**File: todos.py**

- Update read TODO function:

```python
@router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")

    todo_model = db.query(Todos).filter(Todos.id == todo_id)\
                               .filter(Todos.owner_id == user.get('id')).first()

    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail="Todo not found")

```

### 6. Add authentication to update TODO

**File: todos.py**

- Update put request function:

```python
@router.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(user: user_dependency,
                     db: db_dependency,
                     todo_request: TodoRequest,
                     todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")

    todo_model = db.query(Todos).filter(Todos.id == todo_id)\
                               .filter(Todos.owner_id == user.get('id')).first()

    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()

```

### 7. Add authentication to delete TODO

**File: todos.py**

- Update delete function:

```python
@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency,
                     db: db_dependency,
                     todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")

    todo_model = db.query(Todos).filter(Todos.id == todo_id)\
                               .filter(Todos.owner_id == user.get('id')).first()

    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.query(Todos).filter(Todos.id == todo_id)\
                  .filter(Todos.owner_id == user.get('id')).delete()
    db.commit()

```

### 8. Create admin router with special permissions

### 8.1 Update auth.py to include role in JWT

**File: auth.py**

- Update create_access_token function:

```python
def create_access_token(username: str, user_id: int, role: str, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id, 'role': role}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

```

- Update login endpoint:

```python
token = create_access_token(user.username, user.id, user.role, timedelta(minutes=20))

```

- Update get_current_user function:

```python
async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        user_role: str = payload.get('role')
        if username is None or user_id is None:
            raise HTTPException(status_code=401, detail="Could not validate user")
        return {'username': username, 'id': user_id, 'user_role': user_role}
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate user")

```

### 8.2 Create admin.py file

**File: admin.py**

```python
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from models import Todos
from database import SessionLocal
from .auth import get_current_user

router = APIRouter(
    prefix='/admin',
    tags=['admin']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get("/todo", status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401, detail="Authentication Failed")
    return db.query(Todos).all()

@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency,
                     db: db_dependency,
                     todo_id: int = Path(gt=0)):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401, detail="Authentication Failed")

    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()

```

### 8.3 Add admin router to main.py

**File: main.py**

```python
from routers import admin

app.include_router(admin.router)

```

### 9. Create users router for profile and password change

### 9.1 Create users.py file

**File: users.py**

```python
from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from models import Users
from database import SessionLocal
from .auth import get_current_user
from passlib.context import CryptContext

router = APIRouter(
    prefix='/user',
    tags=['user']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)

@router.get("/", status_code=status.HTTP_200_OK)
async def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    return db.query(Users).filter(Users.id == user.get('id')).first()

@router.put("/password", status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user: user_dependency,
                         db: db_dependency,
                         user_verification: UserVerification):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")

    user_model = db.query(Users).filter(Users.id == user.get('id')).first()

    if not bcrypt_context.verify(user_verification.password, user_model.hashed_password):
        raise HTTPException(status_code=401, detail="Error on password change")

    user_model.hashed_password = bcrypt_context.hash(user_verification.new_password)
    db.add(user_model)
    db.commit()

```

### 9.2 Add users router to main.py

**File: main.py**

```python
from routers import users

app.include_router(users.router)

```

### 9.3 Test the application

- Run application:

```bash
uvicorn main:app --reload

```

- Test user profile endpoint
- Test password change endpoint with current and new password

---

## File Structure and Code Summary

### File Structure:

```
project/
├── main.py
├── models.py
├── database.py
├── routers/
│   ├── __init__.py
│   ├── auth.py
│   ├── todos.py
│   ├── admin.py
│   └── users.py

```

### Complete Code Files:

### main.py

```python
from fastapi import FastAPI
from routers import auth, todos, admin, users

app = FastAPI()

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)

```

### Key Authentication Flow:

1. User logs in → receives JWT token with username, user_id, and role
2. JWT token includes user information in payload
3. Each protected endpoint uses user_dependency to validate token
4. Admin endpoints check for 'admin' role
5. User-specific endpoints filter by owner_id
6. Password changes require current password verification

### Testing Commands:

```bash
# Run application
uvicorn main:app --reload

# Access Swagger UI
# Open browser to http://localhost:8000/docs

```
