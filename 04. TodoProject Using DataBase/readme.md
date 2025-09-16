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
