# FastAPI Testing with Pytest - Complete Guide

## What is Testing?

Testing ensures your application works as intended and is part of the Software Development Life Cycle (SDLC).

### Purpose of Testing:

- Identify bugs and defects
- Ensure application meets user requirements
- Guarantee software is high quality, reliable, secure, and user-friendly

## Types of Testing

### 1. Manual Testing

- Testing by running the application yourself
- What we've been doing throughout the course
- Checking if the app looks and works as expected

### 2. Unit Testing

- Tests individual components or units in isolation
- Validates each unit performs as designed
- Automated tests executed by testing frameworks
- Benefits: Identifies bugs early in development

### 3. Integration Testing

- Tests interactions between different units/components
- Broader scope than unit testing
- Tests multiple units working together
- Example: Calling an API endpoint and checking the response

## Pytest Framework

**Pytest** = Popular Python testing framework known for simplicity and scalability

### Why Use Pytest:

- Simple and flexible
- Native assertions
- Fixtures for setup/teardown
- Parameterized testing with different data

## Getting Started with Testing

### Step 1: Project Structure Setup

```
project/
├── test/
│   ├── __init__.py
│   ├── test_example.py
│   └── test_main.py
├── main.py
└── other_files.py

```

### Step 2: Installation

```bash
pip install pytest

```

### Step 3: Naming Conventions

- Test files: Must start with `test_`
- Test functions: Must start with `test_`
- Pytest automatically finds and runs these

## Basic Pytest Assertions

### Simple Equality Tests

```python
def test_equal_or_not_equal():
    assert 3 == 3  # Pass
    assert 3 != 2  # Pass

```

### Instance Testing

```python
def test_is_instance():
    assert isinstance("This is a string", str)  # Pass
    assert not isinstance("10", int)  # Pass (string "10" is not int)

```

### Boolean Testing

```python
def test_boolean():
    validated = True
    assert validated is True
    assert ("hello" == "world") is False

```

### Type Testing

```python
def test_type():
    assert type("hello") is str
    assert type("world") is not int

```

### Comparison Testing

```python
def test_greater_less_than():
    assert 7 > 3
    assert 4 < 10

```

### List Testing

```python
def test_list():
    num_list = [1, 2, 3, 4, 5]
    any_list = [False, False]

    assert 1 in num_list
    assert 7 not in num_list
    assert all(num_list)  # All elements are truthy
    assert not any(any_list)  # No elements are truthy

```

## Working with Objects and Fixtures

### Basic Object Testing

```python
class Student:
    def __init__(self, first_name: str, last_name: str, major: str, years: int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years

def test_person_initialization():
    p = Student("John", "Doe", "Computer Science", 3)
    assert p.first_name == "John", "First name should be John"
    assert p.last_name == "Doe", "Last name should be Doe"
    assert p.major == "Computer Science"
    assert p.years == 3

```

### Using Pytest Fixtures (Better Approach)

```python
import pytest

@pytest.fixture
def default_employee():
    return Student("John", "Doe", "Computer Science", 3)

def test_person_initialization(default_employee):
    assert default_employee.first_name == "John"
    assert default_employee.last_name == "Doe"
    assert default_employee.major == "Computer Science"
    assert default_employee.years == 3

```

**Fixture Benefits**: Reuse objects across multiple tests without recreating them

## Testing FastAPI Applications

### Health Check Endpoint

First, add a simple health check to your FastAPI app:

```python
# main.py
@app.get("/healthy")
def health_check():
    return {"status": "healthy"}

```

### Basic FastAPI Test Setup

```python
# test/test_main.py
from fastapi.testclient import TestClient
from fastapi import status
from ..main import app

client = TestClient(app)

def test_return_health_check():
    response = client.get("/healthy")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "healthy"}

```

## Project Structure for Testing

### Converting to Package Structure

When you get "no module named main" error, restructure your project:

```
FastAPI/                    # Root directory
├── todoapp/               # Your application package
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── routers/
│       ├── __init__.py
│       ├── todos.py
│       └── users.py
└── test/
    ├── __init__.py
    └── test_main.py

```

### Update Imports to Relative Imports

```python
# main.py
from .models import Base
from .database import engine
from .routers import todos, users

# routers/todos.py
from ..models import Todos
from ..database import get_db

```

### Running the Application

```bash
# From FastAPI directory (parent of todoapp)
uvicorn todoapp.main:app --reload

```

## Setting Up Test Database and Dependencies

### ASCII Diagram: Testing Architecture

```
Production Environment          Testing Environment
┌─────────────────────┐        ┌─────────────────────┐
│   Production DB     │        │     Test DB         │
│   (todos_app.db)    │        │   (testdb.db)       │
└─────────────────────┘        └─────────────────────┘
         │                               │
         ▼                               ▼
┌─────────────────────┐        ┌─────────────────────┐
│  Production User    │        │    Mock User        │
│  (JWT validation)   │        │  (fake user data)   │
└─────────────────────┘        └─────────────────────┘
         │                               │
         ▼                               ▼
┌─────────────────────┐        ┌─────────────────────┐
│   FastAPI App       │        │   TestClient        │
│   (live server)     │        │  (test wrapper)     │
└─────────────────────┘        └─────────────────────┘

```

### Test Database Setup

```python
# test/test_todos.py
from sqlalchemy import create_engine, text
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from ..database import Base
from ..main import app

# Create test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./testdb.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create test tables
Base.metadata.create_all(bind=engine)

```

### Dependency Overrides

```python
# Override database dependency
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Override user authentication
def override_get_current_user():
    return {
        "username": "coding_with_devaza_test",
        "id": 1,
        "user_role": "admin"
    }

# Apply overrides
from ..routers.todos import get_db, get_current_user

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

# Create test client
from fastapi.testclient import TestClient
client = TestClient(app)

```

## Testing with Fixtures and Database Cleanup

### Todo Test Fixture

```python
import pytest
from ..models import Todos

@pytest.fixture
def test_todo():
    todo = Todos(
        title="Learn to code",
        description="Need to learn every day",
        priority=5,
        complete=False,
        owner_id=1
    )

    db = TestingSessionLocal()
    db.add(todo)
    db.commit()

    yield db  # Test runs here

    # Cleanup after test
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos"))
        connection.commit()

```

### Testing Read All Todos

```python
def test_read_all_authenticated(test_todo):
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{
        "complete": False,
        "title": "Learn to code",
        "description": "Need to learn every day",
        "id": 1,
        "priority": 5,
        "owner_id": 1
    }]

```

### Testing Read Single Todo

```python
def test_read_one_authenticated(test_todo):
    response = client.get("/todo/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "complete": False,
        "title": "Learn to code",
        "description": "Need to learn every day",
        "id": 1,
        "priority": 5,
        "owner_id": 1
    }

def test_read_one_authenticated_not_found(test_todo):
    response = client.get("/todo/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Todo not found"}

```

### Testing Create Todo

```python
def test_create_todo(test_todo):
    request_data = {
        "title": "New Todo",
        "description": "New todo description",
        "priority": 5,
        "complete": False
    }

    response = client.post("/todo", json=request_data)
    assert response.status_code == 201

    # Verify todo was created in database
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 2).first()

    assert model.title == request_data.get("title")
    assert model.description == request_data.get("description")
    assert model.priority == request_data.get("priority")
    assert model.complete == request_data.get("complete")

```

## Running Tests

### Basic Commands

```bash
# Run all tests
pytest

# Run without warnings
pytest --disable-warnings

# Run specific test file
pytest test/test_todos.py

# Run specific test function
pytest test/test_todos.py::test_read_all_authenticated

```

### Test Output Understanding

```
test/test_example.py ✓✓✓✓✓     [50%]
test/test_main.py ✓           [60%]
test/test_todos.py ✓✓✓✓       [100%]

12 passed in 2.34s

```

## Key Testing Concepts Summary

### Test Isolation

- Each test should be independent
- Use fixtures to set up clean data
- Clean up after each test
- Separate test database from production

### Dependency Injection in Tests

- Override production dependencies
- Mock external services
- Use fake authentication
- Redirect database connections

### Test Structure Pattern

1. **Arrange**: Set up test data (fixtures)
2. **Act**: Execute the code being tested
3. **Assert**: Check the results

### Best Practices

- Use descriptive test names
- Test both success and failure cases
- Keep tests simple and focused
- Use fixtures for reusable setup
- Always clean up test data
- Separate test and production environments

## Common Issues and Solutions

### Import Errors

**Problem**: "No module named main"
**Solution**: Use relative imports and proper package structure

### Database Issues

**Problem**: Tests affecting production data
**Solution**: Use separate test database with dependency overrides

### Authentication Issues

**Problem**: Tests failing due to authentication
**Solution**: Mock authentication with dependency overrides

This guide covers the essential concepts for testing FastAPI applications with Pytest, from basic assertions to complex integration tests with database operations.

# FastAPI Testing Guide - Complete Notes

## Testing Structure Overview

```
project/
├── todo_app/
│   ├── test/
│   │   ├── utils.py          # Reusable testing utilities
│   │   ├── test_todos.py     # Todo endpoints tests
│   │   ├── test_admin.py     # Admin endpoints tests
│   │   ├── test_users.py     # User endpoints tests
│   │   └── test_auth.py      # Authentication tests
│   ├── routers/
│   └── models/

```

## 1. Setting Up Testing Infrastructure

### Database Setup for Testing

**Key Components:**

- **SQLAlchemy**: Database toolkit for Python
- **Test Database**: Separate SQLite database for testing
- **Fixtures**: Reusable test data setup using pytest

```python
# Create separate test database connection
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, poolclass=StaticPool)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

```

### Dependency Overrides

**What it does**: Replaces real dependencies with test versions

- Override database connection to use test database
- Override user authentication to use mock user

```python
# Override database dependency
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Override user authentication
def override_get_current_user():
    return {'username': 'devazatest', 'id': 1, 'user_role': 'admin'}

```

## 2. Creating Reusable Testing Utils

### utils.py File Structure

**Purpose**: Contains all reusable testing code to avoid repetition

**Key Components:**

- Database setup and connections
- Dependency overrides
- Test client setup
- Pytest fixtures for test data

```python
# utils.py example structure
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from app import app

# Database setup
engine = create_engine("sqlite:///./test.db")
TestingSessionLocal = sessionmaker(bind=engine)

# Test client
client = TestClient(app)

# Fixtures for test data
@pytest.fixture
def test_todo():
    # Create test todo, yield it, then cleanup
    pass

```

## 3. Testing Todo Endpoints

### Basic CRUD Operations Testing

**Test Categories:**

1. **Read Operations** (GET requests)
2. **Create Operations** (POST requests)
3. **Update Operations** (PUT requests)
4. **Delete Operations** (DELETE requests)

### Example Test Structure

```python
def test_read_all_authenticated(test_todo):
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == [expected_todo_data]

def test_create_todo(test_todo):
    request_data = {
        "title": "New Todo",
        "description": "New Description",
        "priority": 5,
        "complete": False
    }
    response = client.post("/todos", json=request_data)
    assert response.status_code == 201

```

### Testing Error Scenarios

**Important Test Cases:**

- **404 Not Found**: When requesting non-existent todos
- **401 Unauthorized**: When user lacks permissions
- **Validation Errors**: When request data is invalid

```python
def test_read_one_not_found():
    response = client.get("/todos/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Todo not found"}

```

## 4. Testing Authentication System

### Key Authentication Components

**JWT Tokens**: JSON Web Tokens for secure authentication

- **Encoding**: Converting user data to secure token
- **Decoding**: Extracting user data from token
- **Validation**: Checking if token is valid and not expired

### Testing Authentication Functions

```python
def test_authenticate_user(test_user):
    db = TestingSessionLocal()

    # Test correct credentials
    authenticated_user = authenticate_user("devazatest", "test_password", db)
    assert authenticated_user is not None
    assert authenticated_user.username == "devazatest"

    # Test wrong credentials
    wrong_user = authenticate_user("wrong_username", "test_password", db)
    assert wrong_user is False

```

### Testing Async Functions

**Special Requirements for Async Testing:**

- Install: `pip install pytest-asyncio`
- Use decorator: `@pytest.mark.asyncio`
- Use `await` keyword for async function calls

```python
@pytest.mark.asyncio
async def test_get_current_user_valid_token():
    encode = {"sub": "testuser", "id": 1, "role": "admin"}
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

    user = await get_current_user(token=token)
    assert user == {"username": "testuser", "id": 1, "user_role": "admin"}

```

## 5. Testing User Management

### User Fixture Creation

**Purpose**: Creates test user data before each test runs

```python
@pytest.fixture
def test_user():
    user = Users(
        username="devazatest",
        email="devaza@test.com",
        first_name="Devaza",
        last_name="Test",
        hashed_password=bcrypt_context.hash("test_password"),
        role="admin",
        phone_number="1111111111"
    )
    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user
    # Cleanup after test
    db.execute(text("DELETE FROM users"))
    db.commit()

```

### Testing User Operations

**Common User Tests:**

- Get user profile
- Change password (success and failure scenarios)
- Update phone number
- Validate user data

## 6. Testing Admin Functionality

### Admin Permission Testing

**Key Points:**

- Admin users have elevated permissions
- Test both authorized and unauthorized access
- Verify admin-only operations work correctly

```python
def test_admin_read_all_authenticated(test_todo):
    response = client.get("/admin/todos")
    assert response.status_code == 200
    # Should return all todos for admin user

def test_admin_delete_todo(test_todo):
    response = client.delete("/admin/todos/1")
    assert response.status_code == 204
    # Verify todo was actually deleted from database

```

## 7. Test Organization Best Practices

### File Structure Conventions

**Naming Convention:**

- Test files: `test_[module_name].py`
- Test functions: `test_[function_description]`
- Fixtures: `test_[data_type]` (e.g., `test_user`, `test_todo`)

### Dependency Management

**Import Strategy:**

```python
# In each test file
from .utils import *  # Import all utilities
from ..routers.todos import get_db, get_current_user  # Import specific dependencies

# Override dependencies for the specific module being tested
app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

```

## 8. Running Tests

### Command Line Usage

```bash
# Run all tests
pytest

# Run without warnings
pytest --disable-warnings

# Run specific test file
pytest test_todos.py

# Run with verbose output
pytest -v

```

### Test Status Codes

**Common HTTP Status Codes in Tests:**

- `200 OK`: Successful GET requests
- `201 Created`: Successful POST requests
- `204 No Content`: Successful PUT/DELETE requests
- `401 Unauthorized`: Authentication failures
- `404 Not Found`: Resource doesn't exist

## 9. Database Testing Strategy

### Clean Slate Approach

**Method**: Each test starts with fresh database state

- Create test data before test runs
- Execute test logic
- Clean up all data after test completes

```python
# Cleanup pattern in fixtures
yield test_data  # Provide data to test
with engine.connect() as connection:
    connection.execute(text("DELETE FROM todos"))
    connection.commit()

```

## 10. Error Handling in Tests

### Testing Exception Scenarios

```python
# Test for expected exceptions
with pytest.raises(HTTPException) as exc_info:
    await get_current_user(token="invalid_token")

assert exc_info.value.status_code == 401
assert exc_info.value.detail == "Could not validate user"

```

## Visual Test Flow Diagram

```
Test Execution Flow:
┌─────────────────┐
│  Start Test     │
└─────────┬───────┘
          │
┌─────────▼───────┐
│  Setup Fixture  │ ← Create test data
└─────────┬───────┘
          │
┌─────────▼───────┐
│  Execute Test   │ ← Run actual test logic
└─────────┬───────┘
          │
┌─────────▼───────┐
│  Assert Results │ ← Verify expected outcomes
└─────────┬───────┘
          │
┌─────────▼───────┐
│  Cleanup Data   │ ← Remove test data
└─────────────────┘

```

## Key Testing Concepts

**Mocking**: Replacing real dependencies with fake ones for testing
**Fixtures**: Reusable test data setup and teardown
**Integration Testing**: Testing multiple components working together
**Unit Testing**: Testing individual functions in isolation
**Status Code Assertions**: Verifying HTTP response codes
**JSON Response Testing**: Checking response data structure and content

This testing approach ensures your FastAPI application is reliable, secure, and handles both success and error scenarios correctly.
