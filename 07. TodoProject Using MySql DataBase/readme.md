# MySQL Complete Tutorial - Detailed Study Notes

## What is MySQL?

MySQL is an **open-source relational database management system (RDBMS)** designed for production use.

### Key Characteristics

- **Open Source**: Free to use and modify
- **Relational Database**: Stores data in tables with relationships
- **Server-Based**: Runs on a dedicated server (not embedded)
- **Production-Ready**: Suitable for large-scale applications
- **Highly Scalable**: Can handle massive amounts of data and users
- **Secure**: Enterprise-grade security features

### MySQL vs SQLite Comparison

```
SQLite                          MySQL
┌─────────────────────┐        ┌─────────────────────┐
│ Serverless Database │        │ Server-Based Database│
│ Self-contained      │        │ Requires Server     │
│ Development/Testing │   VS   │ Production Ready    │
│ Single User         │        │ Multi-user Support  │
│ File-based Storage  │        │ Network-based       │
└─────────────────────┘        └─────────────────────┘

```

### Companies Using MySQL

- **Facebook** - Social media platform data management
- **YouTube** - Video metadata and user data
- **Tesla** - Vehicle and manufacturing data systems

## Installation Guide

### Windows Installation Process

### Step 1: Download MySQL

1. **Open Google** and search for "MySQL"
2. **Navigate to** `www.mysql.com`
3. **Hover over Developer Zone** and click
4. **Scroll down** to find "MySQL Downloads"
5. **Click** "MySQL Community Server"
6. **Scroll to** "MySQL Installer for Windows"
7. **Click** "Go to download page"
8. **Select** "Windows (x86, 32-bit), MSI Installer" (web installer - lightweight)
9. **Click** "No thanks, just start my download" (skip login)

### Step 2: Installation Setup

1. **Run the downloaded installer**
2. **Setup Type Selection**:
   - Choose **"Developer Default"**
   - Click **Next**
3. **Path Configuration**:
   - If path exists warning appears, click **Next**
4. **Requirements Check**:
   - System will check for failing requirements
   - Click **Next** (installer resolves automatically)

### Step 3: Product Installation

1. **Download Phase**:
   - MySQL Server, Workbench, Shell, Router will be listed
   - Click **Execute** to download all components
   - If errors appear, keep clicking **Try Again** (common bug)
   - Look for **checkmarks** indicating success
2. **Installation Phase**:
   - Click **Execute** to install all downloaded components
   - Wait for installation to complete (may take time)
   - Click **Next** when finished

### Step 4: MySQL Configuration

1. **Product Configuration**:
   - Click **Next** for product configurations
2. **Network Settings**:
   - **Port**: Leave as **3306** (default)
   - Click **Next**
3. **Authentication**:
   - Choose **"Strong password encryption"** (recommended)
   - Click **Next**
4. **Root User Setup**:
   - **Root Password**: Enter `test1234!`
   - **Add New User**:
     - Username: `admin`
     - Role: **DB Admin** (grants all rights)
     - Password: `test1234!`
   - Click **OK**, then **Next**
5. **System Startup**:
   - Choose whether MySQL starts with system (optional)
   - Click **Next**
6. **Apply Configuration**:
   - Click **Execute**
   - Click **Finish**

### Step 5: Additional Setup

1. **Router Configuration**: Click **Next** (no changes needed)
2. **Samples and Examples**:
   - **Test Connection**:
     - Username: `root`
     - Password: `test1234!`
     - Click **Check** - should show "Connection successful"
   - Click **Next**, **Execute**, **Finish**
3. **Launch Applications**:
   - Check **"Start MySQL Workbench after setup"**
   - Check **"Start MySQL Shell"** (optional)

### Step 6: First Connection Test

1. **MySQL Workbench opens automatically**
2. **Double-click** "Local instance MySQL80"
3. **Enter credentials**:
   - Username: `root`
   - Password: `test1234!`
4. **Click OK** - you should see the main interface with schemas on the left

### Mac Installation Process

### Step 1: Download MySQL for Mac

1. **Open Google** and search for "MySQL"
2. **Navigate to** `www.mysql.com`
3. **Go to Developer Zone**
4. **Scroll to** "MySQL Downloads"
5. **Click** "MySQL Community Server"
6. **Verify Mac OS** is automatically detected (change if needed)
7. **Choose processor type**:
   - **ARM64** - For M1/M2 Macs (newer)
   - **x86_64** - For Intel Macs (older)
8. **Download** the latest DMG archive
9. **Click** "No thanks, just start my download"

### Step 2: Install MySQL Server

1. **Open downloaded DMG file**
2. **Double-click** the MySQL installer package
3. **Installation Process**:
   - Click **Continue**
   - Ensure sufficient disk space
   - Click **Install**
   - **Enter Mac password** when prompted
4. **Server Configuration** (may appear on Intel Macs):
   - **Root Password Setup**: Enter `test1234!`
   - Click **Finish**
   - Check **"Start MySQL Server"**
   - **Enter password again** if prompted
5. **Complete Installation**:
   - Click **Close**
   - **Move to Trash** when asked

### Step 3: Verify MySQL Installation

1. **Click Apple menu** → **System Preferences**
2. **Look for MySQL** icon at bottom
3. **Click MySQL** to see:
   - **Instances tab**: Shows running servers
   - **Configuration tab**: Server settings
4. **Verify server is running** (green indicator)

### Step 4: Install MySQL Workbench

1. **Open new browser tab**
2. **Search** "MySQL Workbench for Mac"
3. **Click** "Download MySQL Workbench"
4. **Select Mac version** and download
5. **Click** "No thanks, just start my download"
6. **Install Workbench**:
   - Open downloaded DMG
   - **Drag MySQL Workbench** to Applications folder
   - Wait for copy to complete

### Step 5: Launch and Connect

1. **Go to Applications** → **MySQL Workbench**
2. **Double-click** to open
3. **Click OK** if security prompt appears
4. **Connect to Database**:
   - **Double-click** "Local instance"
   - **Enter password**: `test1234!`
   - **Click OK**
5. **Verify Connection**: Should see schemas panel on left

## Database and Table Creation

### Creating Application Database

### Step 1: Create New Schema (Database)

1. **In MySQL Workbench**, locate **Schemas panel** (left side)
2. **Right-click** in empty area of Schemas panel
3. **Select** "Create Schema"
4. **Schema Configuration**:
   - **Name**: `todo_application_database`
   - Leave other settings as default
5. **Click** "Apply"
6. **Review SQL**: `CREATE SCHEMA todo_application_database;`
7. **Click** "Apply" again
8. **Click** "Close"

### Step 2: Connect to New Database

1. **Double-click** `todo_application_database` in Schemas panel
2. **Database becomes highlighted** (indicates active connection)
3. **Expand database** to see Tables, Views, etc.

### Database Schema Design

### Entity Relationship Structure

```
todo_application_database
├── Tables
│   ├── users
│   │   ├── id (PRIMARY KEY, AUTO_INCREMENT)
│   │   ├── email (VARCHAR 200)
│   │   ├── username (VARCHAR 45)
│   │   ├── first_name (VARCHAR 45)
│   │   ├── last_name (VARCHAR 45)
│   │   ├── hashed_password (VARCHAR 200)
│   │   ├── is_active (BOOLEAN)
│   │   └── role (VARCHAR 45)
│   └── todos
│       ├── id (PRIMARY KEY, AUTO_INCREMENT)
│       ├── title (VARCHAR 200)
│       ├── description (VARCHAR 200)
│       ├── priority (INTEGER)
│       ├── complete (BOOLEAN)
│       └── owner_id (FOREIGN KEY → users.id)

```

### SQL Table Creation Scripts

### Step 1: Open SQL Editor

1. **Click** the SQL editor icon (lightning bolt or "+" tab)
2. **New SQL query tab** opens

### Step 2: Create Users Table

```sql
-- Drop existing users table if it exists (safety measure)
DROP TABLE IF EXISTS users;

-- Create users table with all required fields
CREATE TABLE users (
    id INT(11) NOT NULL AUTO_INCREMENT,        -- Primary key, auto-incrementing
    email VARCHAR(200),                        -- User email address
    username VARCHAR(45),                      -- User login name
    first_name VARCHAR(45),                    -- User's first name
    last_name VARCHAR(45),                     -- User's last name
    hashed_password VARCHAR(200),              -- Encrypted password
    is_active BOOLEAN,                         -- Account status flag
    role VARCHAR(45),                          -- User role (admin, user, etc.)
    PRIMARY KEY (id)                           -- Define primary key
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

```

### Step 3: Create Todos Table

```sql
-- Drop existing todos table if it exists
DROP TABLE IF EXISTS todos;

-- Create todos table with foreign key relationship
CREATE TABLE todos (
    id INT(11) NOT NULL AUTO_INCREMENT,        -- Primary key, auto-incrementing
    title VARCHAR(200),                        -- Task title
    description VARCHAR(200),                  -- Task description
    priority INT(11),                          -- Priority level (1-5)
    complete BOOLEAN,                          -- Completion status
    owner_id INT(11),                          -- Foreign key to users table
    PRIMARY KEY (id),                          -- Define primary key
    FOREIGN KEY (owner_id) REFERENCES users(id) -- Link to users table
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

```

### Step 4: Execute SQL Scripts

1. **Copy and paste** both table creation scripts
2. **Click lightning bolt icon** to execute
3. **Check output**: Should show successful table creation
4. **Right-click** "Tables" in schema → **Refresh All**
5. **Verify**: Should see `users` and `todos` tables

### SQL Data Types Explained

### INT(11) AUTO_INCREMENT

- **INT**: Integer number data type
- **(11)**: Display width (cosmetic, doesn't limit size)
- **AUTO_INCREMENT**: Automatically generates unique numbers (1, 2, 3...)
- **Primary use**: Primary keys

### VARCHAR(n)

- **Variable Character**: Text/string data type
- **n**: Maximum number of characters
- **VARCHAR(200)**: Up to 200 characters
- **Efficient**: Only uses space needed

### BOOLEAN

- **True/False values**
- **MySQL stores as**: TINYINT (0 = false, 1 = true)
- **Common uses**: Status flags, completion indicators

### ENGINE=InnoDB

- **InnoDB**: MySQL storage engine
- **Features**: ACID compliance, foreign keys, transactions
- **Default**: Recommended for production use

### CHARSET=latin1

- **Character encoding**: How text is stored
- **latin1**: Western European characters
- **Modern alternative**: utf8mb4 (supports all Unicode)

## Application Integration

### Installing MySQL Python Driver

### Install PyMySQL Package

```bash
# Install Python MySQL connector
#run this

pip install pymysql

#if not work run this

pip install pymysql==1.0.3

```

**PyMySQL**: Pure Python MySQL client library that allows Python applications to connect to MySQL databases.

### Database Connection Configuration

### Connection String Format

```
mysql+pymysql://username:password@host:port/database_name

```

### Updated Database Configuration

```python
# database.py - MySQL connection setup

# Old SQLite connection (remove this)
# SQLALCHEMY_DATABASE_URL = "sqlite:///./todos_app.db"

# New MySQL connection
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:test1234!@127.0.0.1:3306/todo_application_database"

```

### Connection String Breakdown

```
mysql+pymysql://root:test1234!@127.0.0.1:3306/todo_application_database
     ↓         ↓      ↓         ↓         ↓              ↓
  database   dialect user    password   host:port    database_name
   type                                  (localhost)

```

### Remove SQLite-Specific Code

```python
# Remove this SQLite-only parameter
# connect_args={"check_same_thread": False}

# Clean MySQL engine creation
engine = create_engine(SQLALCHEMY_DATABASE_URL)

```

### Testing Database Integration

### Step 1: Start FastAPI Application

```bash
# Start development server with auto-reload
uvicorn main:app --reload

```

### Step 2: Create Test Users

**User 1 - Admin User**:

```json
{
  "username": "coding_with_ruby",
  "email": "coding_with_ruby@gmail.com",
  "first_name": "devaza",
  "last_name": "Robi",
  "password": "test1234",
  "role": "admin"
}
```

**Expected Response**: `201 Created` with null body

**User 2 - Regular User**:

```json
{
  "username": "example_user_1",
  "email": "example_user_1@email.com",
  "first_name": "Example",
  "last_name": "User",
  "password": "test1234",
  "role": "user"
}
```

### Step 3: Verify User Creation in MySQL

```sql
-- Query to check created users
SELECT * FROM users;

```

**Expected Results**:

```
| id | email                      | username         | first_name | last_name | hashed_password | is_active | role  |
|----|----------------------------|------------------|------------|-----------|-----------------|-----------|-------|
| 1  | coding_with_ruby@gmail.com | coding_with_ruby | devaza     | Robi      | [hashed]        | 1         | admin |
| 2  | example_user_1@email.com   | example_user_1   | Example    | User      | [hashed]        | 1         | user  |

```

### Step 4: Create Test Todos

**Authentication Required**:

1. **Click "Authorize"** in FastAPI docs
2. **Login** with `coding_with_ruby` credentials
3. **Get JWT token** for authenticated requests

**Create Todo**:

```json
{
  "title": "Learn Fast API",
  "description": "Because it is awesome",
  "priority": 5,
  "complete": true
}
```

### Step 5: Verify Todo Creation

```sql
-- Query to check created todos
SELECT * FROM todos;

```

**Expected Results**:

```
| id | title          | description          | priority | complete | owner_id |
|----|----------------|---------------------|----------|----------|----------|
| 1  | Learn Fast API | Because it is awesome| 5        | 1        | 1        |

```

### Understanding Foreign Key Relationship

### Visual Relationship Diagram

```
users table                     todos table
┌─────────────────┐            ┌─────────────────┐
│ id (PK) │   1   │◄───────────┤ owner_id (FK)   │
│ username│ admin │            │ id (PK)    │ 1  │
│ email   │ ...   │            │ title      │... │
│ ...     │ ...   │            │ description│... │
└─────────────────┘            │ priority   │... │
                               │ complete   │... │
                               └─────────────────┘

```

**Explanation**:

- **PK (Primary Key)**: Unique identifier for each record
- **FK (Foreign Key)**: References primary key in another table
- **owner_id**: Links each todo to a specific user
- **Data Integrity**: Can't create todo for non-existent user

## Database Management

### Cleaning Up Development Files

### Remove SQLite Database File

```bash
# Delete SQLite database (if switching to MySQL)
rm todos_app.db

```

**Why Remove**:

- `todos_app.db` was created for SQLite
- Not needed when using MySQL
- Prevents confusion between database systems

### Switching Between Databases

**To use SQLite** (development):

```python
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos_app.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

```

**To use MySQL** (production):

```python
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:test1234!@127.0.0.1:3306/todo_application_database"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

```

## Complete Code Examples with Detailed Explanations

### 1. Database Connection Configuration

```python
# database.py - MySQL database connection setup
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MySQL connection string with authentication
# Format: mysql+pymysql://user:password@host:port/database
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:test1234!@127.0.0.1:3306/todo_application_database"

# Create database engine for MySQL
# Engine manages connection pool and database connections
# No connect_args needed (SQLite-specific parameter removed)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create session factory for database operations
# SessionLocal creates new database session instances
# autocommit=False: Require explicit commit for transactions
# autoflush=False: Don't automatically flush changes
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for ORM models
# All database models will inherit from this base
Base = declarative_base()

```

### 2. Database Models Definition

```python
# models.py - SQLAlchemy ORM models for MySQL
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Users(Base):
    """
    Users model representing user accounts
    Maps to 'users' table in MySQL database
    """
    __tablename__ = "users"  # Specify MySQL table name

    # Primary key with auto-increment (INT AUTO_INCREMENT)
    id = Column(Integer, primary_key=True, index=True)

    # User email - VARCHAR(200) in MySQL
    email = Column(String(200), nullable=True)

    # Username for login - VARCHAR(45) in MySQL
    username = Column(String(45), nullable=False)

    # User's first name - VARCHAR(45) in MySQL
    first_name = Column(String(45), nullable=False)

    # User's last name - VARCHAR(45) in MySQL
    last_name = Column(String(45), nullable=False)

    # Hashed password storage - VARCHAR(200) in MySQL
    hashed_password = Column(String(200), nullable=False)

    # Account activation status - BOOLEAN (TINYINT in MySQL)
    is_active = Column(Boolean, default=True)

    # User role (admin, user, etc.) - VARCHAR(45) in MySQL
    role = Column(String(45), nullable=False)

    # One-to-many relationship: one user can have many todos
    # back_populates creates bidirectional relationship
    todos = relationship("Todos", back_populates="owner")

class Todos(Base):
    """
    Todos model representing task/todo items
    Maps to 'todos' table in MySQL database
    """
    __tablename__ = "todos"  # Specify MySQL table name

    # Primary key with auto-increment (INT AUTO_INCREMENT)
    id = Column(Integer, primary_key=True, index=True)

    # Task title - VARCHAR(200) in MySQL
    title = Column(String(200), nullable=False)

    # Task description - VARCHAR(200) in MySQL
    description = Column(String(200), nullable=True)

    # Priority level (1-5 scale) - INT in MySQL
    priority = Column(Integer, nullable=False)

    # Completion status - BOOLEAN (TINYINT in MySQL)
    complete = Column(Boolean, default=False)

    # Foreign key referencing users.id - INT in MySQL
    # Creates relationship between todos and users
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Many-to-one relationship: many todos belong to one user
    # back_populates creates bidirectional relationship
    owner = relationship("Users", back_populates="todos")

```

### 3. Database Session Management

```python
# dependencies.py - Database session dependency injection
from database import SessionLocal

def get_db():
    """
    Database session dependency for FastAPI
    Creates new session for each request
    Ensures proper cleanup after request completion
    """
    # Create new database session
    db = SessionLocal()
    try:
        # Yield session to route handler
        # Using yield makes this a generator function
        # FastAPI will inject this into route parameters
        yield db
    finally:
        # Always close session after request
        # Prevents connection leaks and resource exhaustion
        db.close()

```

### 8. MySQL Database Queries for Testing

```sql
-- Check all users in the database
SELECT
    id,
    email,
    username,
    first_name,
    last_name,
    is_active,
    role
FROM users
ORDER BY id;

-- Check all todos with user information
SELECT
    t.id,
    t.title,
    t.description,
    t.priority,
    t.complete,
    t.owner_id,
    u.username,
    u.first_name,
    u.last_name
FROM todos t
LEFT JOIN users u ON t.owner_id = u.id
ORDER BY t.id;

-- Count todos by user
SELECT
    u.username,
    COUNT(t.id) as todo_count
FROM users u
LEFT JOIN todos t ON u.id = t.owner_id
GROUP BY u.id, u.username
ORDER BY todo_count DESC;

-- Find completed todos
SELECT
    t.title,
    t.description,
    u.username
FROM todos t
JOIN users u ON t.owner_id = u.id
WHERE t.complete = 1
ORDER BY t.id;

-- Find high priority incomplete todos
SELECT
    t.id,
    t.title,
    t.priority,
    u.username
FROM todos t
JOIN users u ON t.owner_id = u.id
WHERE t.complete = 0 AND t.priority >= 4
ORDER BY t.priority DESC;

-- Get user statistics
SELECT
    u.username,
    u.role,
    COUNT(t.id) as total_todos,
    SUM(CASE WHEN t.complete = 1 THEN 1 ELSE 0 END) as completed_todos,
    SUM(CASE WHEN t.complete = 0 THEN 1 ELSE 0 END) as pending_todos
FROM users u
LEFT JOIN todos t ON u.id = t.owner_id
GROUP BY u.id, u.username, u.role
ORDER BY total_todos DESC;

```
