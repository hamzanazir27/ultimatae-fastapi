# PostgreSQL Complete Tutorial - Detailed Study Notes

--

## What is PostgreSQL?

PostgreSQL is a **production-grade database** (unlike SQLite which is for development/testing).

### Key Features

- **Open source relational database management system (RDBMS)**
- **Secure database** with enterprise-level security
- **Requires a server** (opposite of SQLite which is serverless)
- **Highly scalable** for large numbers of users
- **Production-ready** for real-world applications

### Companies Using PostgreSQL

- **Apple** - Uses PostgreSQL for various services
- **Reddit** - Powers their massive user base
- **Twitch** - Handles streaming data and user interactions

## PostgreSQL vs SQLite Comparison

```
SQLite                          PostgreSQL
┌─────────────────────┐        ┌─────────────────────┐
│ Serverless Database │        │ Server-Based Database│
│ Self-contained      │        │ Requires Setup      │
│ Development/Testing │   VS   │ Production Ready    │
│ Limited Users       │        │ Unlimited Scaling   │
│ Simple Setup        │        │ More Configuration  │
└─────────────────────┘        └─────────────────────┘

```

## Installation Guide

### Windows Installation Steps

### Step 1: Download PostgreSQL

1. Go to **postgresql.org**
2. Click **Download**
3. Select **Windows**
4. Choose **Installer** (easiest method)
5. Download **version 14.1** (or latest available)

### Step 2: Installation Process

1. **Run the installer**
2. **Welcome screen** → Click Next
3. **Installation directory** → Use default: `C:\Program Files\PostgreSQL\14`
4. **Select components**:
   - ✅ PostgreSQL Server (database engine)
   - ✅ pgAdmin 4 (graphical user interface)
   - ✅ Command Line Tools
   - ✅ Stack Builder (optional tools)
5. **Data directory** → Use default with `/data` folder
6. **Set superuser password** → Create a strong password (remember this!)
7. **Port number** → Use default **5432**
8. **Locale** → Use default
9. **Install** → Wait for completion

### Step 3: Post-Installation

1. **Stack Builder** appears (optional)
   - Can install additional tools
   - Skip for basic setup
2. **pgAdmin 4** automatically installed
   - Graphical interface for database management
   - Access via Windows Start Menu

### Mac Installation Steps

### Step 1: Download PostgreSQL App

1. Go to **postgresql.org**
2. Click **Download** → **Mac**
3. Find **Postgres.app** section
4. Click **Download the Universal**
5. Download the **DMG file**

### Step 2: Install PostgreSQL App

1. **Open DMG file**
2. **Drag Postgres.app to Applications folder**
3. **Launch Postgres.app**
4. **Click Initialize** when prompted
5. **Grant permissions** if requested

### Step 3: Setup Command Line Access

1. **Open Terminal**
2. **Copy and paste** the PATH command from Postgres.app
3. **Enter your Mac password** when prompted

### Step 4: Install pgAdmin (GUI Tool)

1. **Download pgAdmin 4** from pgadmin.org
2. **Select Mac OS version**
3. **Install DMG file**
4. **Drag pgAdmin to Applications**
5. **Set master password** when first launched

## Database Setup and Configuration

### Creating a Production Database

### Step 1: Access pgAdmin

1. **Open pgAdmin 4**
2. **Enter master password**
3. **Locate Servers group** (created by default)

### Step 2: Register New Server

1. **Right-click Servers** → Register → Server
2. **General Tab**:
   - Name: `ToDo Application Server`
   - Server Group: `Servers`
   - Connect now: ✅ Checked
3. **Connection Tab**:
   - Host: `localhost`
   - Port: `5432`
   - Username: `postgres`
   - Password: `[your password]`
4. **Click Save**

### Step 3: Verify Super User Access

1. **Expand server** → Login/Group Roles
2. **Find postgres user**
3. **Right-click** → Properties → Privileges
4. **Verify superuser** privileges are enabled

### Creating Application Database

### Step 1: Create New Database

1. **Right-click Databases** → Create → Database
2. **General Tab**:
   - Database: `TODO_application_database`
   - Owner: `postgres`
3. **Click Save**

### Step 2: Connect to Database

- Database **automatically connects**
- If not connected: **Right-click** → Connect to database

## Database Schema Creation

### Understanding Database Structure

```
TODO_application_database
├── Schemas
│   └── public
│       └── Tables
│           ├── users (user accounts)
│           └── todos (task items)

```

### Creating Tables with SQL

### Step 1: Open Query Tool

1. **Click Query Tool** icon (top toolbar)
2. **SQL editor opens** for writing commands

### Step 2: Users Table Creation

**Purpose**: Store user account information

**SQL Code**:

```sql
-- Remove table if it already exists
DROP TABLE IF EXISTS users;

-- Create users table with all required fields
CREATE TABLE users (
    id SERIAL,                          -- Auto-incrementing primary key
    email VARCHAR(200) DEFAULT NULL,    -- Email address (200 chars max)
    username VARCHAR(45),               -- Username (45 chars max)
    first_name VARCHAR(45),             -- First name (45 chars max)
    last_name VARCHAR(45),              -- Last name (45 chars max)
    hashed_password VARCHAR(200),       -- Encrypted password
    is_active BOOLEAN,                  -- Account status (true/false)
    role VARCHAR(45),                   -- User role (admin, user, etc.)
    PRIMARY KEY (id)                    -- Set id as primary key
);

```

### Step 3: ToDos Table Creation

**Purpose**: Store task/todo items with user relationship

**SQL Code**:

```sql
-- Remove table if it already exists
DROP TABLE IF EXISTS todos;

-- Create todos table with foreign key relationship
CREATE TABLE todos (
    id SERIAL,                          -- Auto-incrementing primary key
    title VARCHAR(200),                 -- Task title
    description VARCHAR(200),           -- Task description
    priority INTEGER,                   -- Priority level (1-5)
    complete BOOLEAN,                   -- Completion status
    owner_id INTEGER,                   -- Links to users.id
    PRIMARY KEY (id),                   -- Set id as primary key
    FOREIGN KEY (owner_id) REFERENCES users(id)  -- Link to users table
);

```

### Key SQL Concepts Explained

### SERIAL Data Type

- **PostgreSQL-specific** data type
- **Combines**: INTEGER + AUTO_INCREMENT + PRIMARY KEY
- **Automatically generates** unique numbers (1, 2, 3, ...)

### VARCHAR Data Type

- **Variable character** = text/string
- **VARCHAR(200)** = maximum 200 characters
- **Flexible length** (uses only space needed)

### FOREIGN KEY Relationship

- **Links tables together**
- **owner_id** in todos → **id** in users
- **Ensures data integrity** (can't create todo for non-existent user)

## Application Integration

### Installing Required Dependencies

### Python Package Installation

```bash
# Install PostgreSQL adapter for Python
pip install psycopg2-binary==2.9.6

```

**psycopg2-binary**: Python library that allows Python applications to connect to PostgreSQL databases.

### Database Connection Configuration

### Step 1: Update Connection String

**File**: `database.py` or similar database configuration file

**Old SQLite Connection**:

```python
# SQLite connection (file-based)
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

```

**New PostgreSQL Connection**:

```python
# PostgreSQL connection (server-based)
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:test1234!@localhost/TODO_application_database"

```

**Connection String Breakdown**:

```
postgresql://username:password@host:port/database_name
     ↓         ↓        ↓       ↓    ↓        ↓
  database   user    password  host port  database
   type                              (5432) name

```

### Step 2: Remove SQLite-Specific Code

**Before (SQLite)**:

```python
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # SQLite only
)

```

**After (PostgreSQL)**:

```python
engine = create_engine(SQLALCHEMY_DATABASE_URL)  # No extra args needed

```

## Testing the Database Connection

### Step 1: Start the Application

```bash
# Start FastAPI development server
uvicorn main:app --reload

```

### Step 2: Create Test Users

### User 1 (Admin User)

```json
{
  "username": "coding_with_ruby",
  "email": "coding_with_ruby@gmail.com",
  "first_name": "devaza",
  "last_name": "Ruby",
  "password": "test1234",
  "role": "admin"
}
```

### User 2 (Regular User)

```json
{
  "username": "example_user_1",
  "email": "example_user_1@gmail.com",
  "first_name": "Example",
  "last_name": "User",
  "password": "test1234",
  "role": "user"
}
```

### Step 3: Verify Database Records

**Check Users Table**:

```sql
SELECT * FROM users;

```

**Expected Results**:

```
id | email                           | username          | first_name | last_name
---|--------------------------------|-------------------|------------|----------
1  | coding_with_ruby@gmail.com     | coding_with_ruby  | devaza     | Ruby
2  | example_user_1@gmail.com       | example_user_1    | Example    | User

```

### Step 4: Create Test ToDos

### Authorize User

1. **Use authentication endpoint**
2. **Login with** `coding_with_ruby` credentials
3. **Get authorization token**

### Create ToDo Item

```json
{
  "title": "Learn Fast API",
  "description": "Because it's awesome",
  "priority": 5,
  "complete": true
}
```

### Step 5: Verify ToDo Creation

**Check ToDos Table**:

```sql
SELECT * FROM todos;

```

**Expected Results**:

```
id | title          | description          | priority | complete | owner_id
---|----------------|---------------------|----------|----------|----------
1  | Learn Fast API | Because it's awesome | 5        | true     | 1

```

## Database Relationship Verification

### Understanding Foreign Key Relationship

```
users table                    todos table
┌──────────────┐              ┌──────────────┐
│ id (PK) │ 1  │◄─────────────┤ owner_id(FK) │
│ username│...  │              │ title       │
│ email   │...  │              │ description │
└──────────────┘              │ priority    │
                              │ complete    │
                              └──────────────┘

```

**PK = Primary Key** (unique identifier)
**FK = Foreign Key** (references another table)

## Production vs Development Database

### When to Switch to PostgreSQL

### Stay with SQLite if:

- **Small application** (< 1000 users)
- **Single developer**
- **Simple requirements**
- **Quick prototyping**

### Switch to PostgreSQL if:

- **Growing user base** (> 1000 users)
- **Multiple developers**
- **Production deployment**
- **Advanced features needed**

### Migration Benefits

### Performance Improvements

- **Better concurrent access** (multiple users)
- **Optimized queries** for large datasets
- **Advanced indexing** capabilities
- **Connection pooling** support

### Advanced Features

- **Full-text search**
- **JSON data types**
- **Custom functions**
- **Triggers and procedures**
- **Replication support**

## Complete Code Examples with Detailed Explanations

### 1. Database Connection Configuration

```python
# database.py - Database connection setup
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL connection string format:
# postgresql://username:password@host:port/database_name
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:test1234!@localhost/TODO_application_database"

# Create database engine
# Engine manages connection pool and database connections
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create session factory
# SessionLocal creates database session instances
# autocommit=False: Manual transaction control
# autoflush=False: Manual flush control
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for database models
# All database models inherit from this base
Base = declarative_base()

```

### 2. User Model Definition

```python
# models.py - Database model definitions
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Users(Base):
    """
    User model for storing user account information
    Maps to 'users' table in PostgreSQL database
    """
    __tablename__ = "users"  # Specify table name

    # Primary key - auto-incrementing integer
    id = Column(Integer, primary_key=True, index=True)

    # User email - variable length string, max 200 chars
    email = Column(String(200), nullable=True)

    # Username - required field, max 45 chars
    username = Column(String(45), nullable=False)

    # User's first name - max 45 chars
    first_name = Column(String(45), nullable=False)

    # User's last name - max 45 chars
    last_name = Column(String(45), nullable=False)

    # Encrypted password - max 200 chars for hash
    hashed_password = Column(String(200), nullable=False)

    # Account active status - boolean true/false
    is_active = Column(Boolean, default=True)

    # User role (admin, user, etc.) - max 45 chars
    role = Column(String(45), nullable=False)

    # Relationship to todos - one user can have many todos
    # back_populates creates bidirectional relationship
    todos = relationship("Todos", back_populates="owner")

```

### 3. ToDo Model Definition

```python
class Todos(Base):
    """
    Todo model for storing task/todo items
    Maps to 'todos' table in PostgreSQL database
    """
    __tablename__ = "todos"  # Specify table name

    # Primary key - auto-incrementing integer
    id = Column(Integer, primary_key=True, index=True)

    # Task title - variable length string, max 200 chars
    title = Column(String(200), nullable=False)

    # Task description - variable length string, max 200 chars
    description = Column(String(200), nullable=True)

    # Priority level - integer (typically 1-5 scale)
    priority = Column(Integer, nullable=False)

    # Completion status - boolean true/false
    complete = Column(Boolean, default=False)

    # Foreign key linking to users table
    # References users.id to establish relationship
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Relationship to user - many todos belong to one user
    # back_populates creates bidirectional relationship
    owner = relationship("Users", back_populates="todos")

```

### 4. Database Session Dependency

```python
# dependencies.py - Database session management
from database import SessionLocal

def get_db():
    """
    Dependency function to create database session
    Used with FastAPI dependency injection
    Ensures proper session cleanup after request
    """
    # Create new database session
    db = SessionLocal()
    try:
        # Yield session to route handler
        # 'yield' makes this a generator function
        yield db
    finally:
        # Always close session after use
        # Prevents connection leaks
        db.close()

```

### 5. User Creation Endpoint

```python
# routes/auth.py - User authentication routes
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models import Users
from dependencies import get_db
from passlib.context import CryptContext

# Password hashing context
# Uses bcrypt algorithm for secure password hashing
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()

@router.post("/auth/create-user", status_code=status.HTTP_201_CREATED)
async def create_user(
    create_user_request: CreateUserRequest,  # Request body model
    db: Session = Depends(get_db)  # Database session dependency
):
    """
    Create new user account
    Validates unique email/username and hashes password
    """

    # Check if email already exists
    existing_user = db.query(Users).filter(
        Users.email == create_user_request.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    # Create new user model instance
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        # Hash password before storing
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True,
        role=create_user_request.role
    )

    # Add user to database session
    db.add(create_user_model)

    # Commit transaction to save to database
    db.commit()

    # Return success response
    return {"message": "User created successfully"}

```

### 6. ToDo Creation Endpoint

```python
# routes/todos.py - Todo CRUD operations
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models import Todos
from dependencies import get_db, get_current_user

router = APIRouter()

@router.post("/todos", status_code=status.HTTP_201_CREATED)
async def create_todo(
    todo_request: CreateTodoRequest,  # Request body model
    user: dict = Depends(get_current_user),  # Current authenticated user
    db: Session = Depends(get_db)  # Database session dependency
):
    """
    Create new todo item for authenticated user
    Automatically links todo to current user via owner_id
    """

    # Create new todo model instance
    todo_model = Todos(
        title=todo_request.title,
        description=todo_request.description,
        priority=todo_request.priority,
        complete=todo_request.complete,
        # Link todo to current user
        owner_id=user.get("id")
    )

    # Add todo to database session
    db.add(todo_model)

    # Commit transaction to save to database
    db.commit()

    # Return success response
    return {"message": "Todo created successfully"}

```

### 7. Database Query Examples

```python
# Example queries for common operations

def get_all_users(db: Session):
    """
    Retrieve all users from database
    Returns list of User objects
    """
    return db.query(Users).all()

def get_user_by_id(db: Session, user_id: int):
    """
    Retrieve single user by ID
    Returns User object or None if not found
    """
    return db.query(Users).filter(Users.id == user_id).first()

def get_todos_by_user(db: Session, user_id: int):
    """
    Retrieve all todos for specific user
    Uses foreign key relationship
    """
    return db.query(Todos).filter(Todos.owner_id == user_id).all()

def update_todo_status(db: Session, todo_id: int, complete: bool):
    """
    Update todo completion status
    Uses update() method for efficient updates
    """
    db.query(Todos).filter(Todos.id == todo_id).update(
        {"complete": complete}
    )
    db.commit()

def delete_todo(db: Session, todo_id: int):
    """
    Delete todo from database
    Uses delete() method
    """
    todo = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo:
        db.delete(todo)
        db.commit()
        return True
    return False

```

## Summary

This comprehensive guide covers:

1. **PostgreSQL installation** on Windows and Mac
2. **Database setup** and configuration
3. **Table creation** with proper relationships
4. **Application integration** with Python/FastAPI
5. **Complete code examples** with detailed explanations
6. **Best practices** for production database management

**Key Takeaways**:

- PostgreSQL is **production-ready** and **highly scalable**
- **Foreign key relationships** ensure data integrity
- **SQLAlchemy ORM** simplifies database operations
- **Proper session management** prevents connection issues
- **Password hashing** ensures security
- **Dependency injection** promotes clean code architecture
