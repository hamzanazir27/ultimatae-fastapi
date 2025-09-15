dd# FastAPI Project 2 - Complete Study Notes

## Main Headings from the Document:

1. **Overview**
2. **CRUD Operations & HTTP Methods**
3. **Project Setup**
4. **Creating Book Objects**
5. **POST Request Method (Basic)**
6. **Data Validation with Pydantic**
7. **BookRequest Model**
8. **Field Validation**
9. **Improved POST Method**
10. **Auto-ID Assignment**
11. **Model Configuration**
12. **Key Concepts Explained**
13. **Complete Working Code Structure**
14. **Error Handling**
15. **Testing with Swagger UI**
16. **Summary of Key Benefits**
17. **Getting Book by ID**
18. **Filtering Books by Rating**
19. **Updating Books (PUT Request)**
20. **Deleting Books (DELETE Request)**
21. **Adding Published Date Field**
22. **Path Parameter Validation**
23. **Query Parameter Validation**
24. **HTTP Status Codes**
25. **HTTP Exceptions**
26. **Custom Status Code Responses**
27. **Complete API Architecture**

The notes comprehensively cover building a FastAPI application with full CRUD operations, data validation using Pydantic, proper HTTP status codes, exception handling, and professional API development practices.

- **CRUD**: CREATE→POST, READ→GET, UPDATE→PUT, DELETE→DELETE
- **Pydantic**: Data validation library (comes with FastAPI)
- **Status Codes**: 200 (OK), 201 (Created), 204 (No Content), 404 (Not Found), 422 (Validation Error)

# Short Notes Main Points

## Core Concepts

- **CRUD**: CREATE→POST, READ→GET, UPDATE→PUT, DELETE→DELETE
- **Pydantic**: Data validation library (comes with FastAPI)
- **Status Codes**: 200 (OK), 201 (Created), 204 (No Content), 404 (Not Found), 422 (Validation Error)

## Basic Setup

```python
from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()
books = []

```

## Models

```python
# Storage class
class Book:
    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

# Validation class
class BookRequest(BaseModel):
    id: Optional[int] = Field(default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)  # 1-5 rating

```

## CRUD Endpoints

```python
# GET all books
@app.get("/books", status_code=200)
async def read_all_books():
    return books

# GET book by ID
@app.get("/books/{book_id}", status_code=200)
async def read_book(book_id: int = Path(gt=0)):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found")

# GET by rating (query parameter)
@app.get("/books/", status_code=200)
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    return [book for book in books if book.rating == book_rating]

# POST new book
@app.post("/create-book", status_code=201)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    new_book.id = 1 if len(books) == 0 else books[-1].id + 1
    books.append(new_book)

# PUT update book
@app.put("/books/update_book", status_code=204)
async def update_book(book: BookRequest):
    for i in range(len(books)):
        if books[i].id == book.id:
            books[i] = book
            return
    raise HTTPException(status_code=404, detail="Item not found")

# DELETE book
@app.delete("/books/{book_id}", status_code=204)
async def delete_book(book_id: int = Path(gt=0)):
    for i in range(len(books)):
        if books[i].id == book_id:
            books.pop(i)
            return
    raise HTTPException(status_code=404, detail="Item not found")

```

## Key Validation Rules

- **Path**: `Path(gt=0)` - ID must be > 0
- **Query**: `Query(gt=0, lt=6)` - Rating 1-5
- **Field**: `Field(min_length=3)` - Title min 3 chars
- **Field**: `Field(gt=0, lt=6)` - Rating 1-5

## Error Handling

```python
# Raise 404 when item not found
raise HTTPException(status_code=404, detail="Item not found")

```

## Run Command

```bash
uvicorn books2:app --reload

```

## Swagger UI

Access at: `http://localhost:8000/docs`

## Quick Tips

- Use `*book_request.model_dump()` to convert Pydantic to dict
- `Optional[int] = None` makes fields optional
- Break after deletion: `books.pop(i); break`
- Auto-ID: `books[-1].id + 1` for next ID

---

# Detailed Notes

## Overview

Project 2 builds upon Project 1 by creating more sophisticated book API endpoints with real Python objects, data validation, and professional FastAPI features.

### What We'll Learn

- **HTTP Methods**: GET, POST, PUT, DELETE
- **New Concepts**: Data validation, exception handling, status codes, Swagger configuration, Python request objects
- **Key Technology**: Pydantic for data validation

---

## CRUD Operations & HTTP Methods

```
CREATE → POST   (Create new resources)
READ   → GET    (Retrieve existing resources)
UPDATE → PUT    (Modify existing resources)
DELETE → DELETE (Remove resources)

```

---

## Project Setup

### 1. Create New Python File

```python
# books2.py
from fastapi import FastAPI

app = FastAPI()
books = []  # Empty list to store book objects

```

### 2. Basic GET Endpoint

```python
@app.get("/books")
async def read_all_books():
    return books

```

### 3. Run Application

```bash
uvicorn books2:app --reload

```

---

## Creating Book Objects

### Book Class Structure

```python
class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

```

### Sample Data Creation

```python
books = [
    Book(1, "Computer Science Pro", "Coding with Ruby", "A very nice book", 5),
    Book(2, "Be Fast with FastAPI", "Coding with Ruby", "This is a great book", 5),
    Book(3, "Master Endpoints", "Coding with Ruby", "This is an awesome book", 5),
    Book(4, "HP1", "Author One", "Book description", 2),
    Book(5, "HP2", "Author Two", "Book description", 3),
    Book(6, "HP3", "Author Three", "Book description", 1)
]

```

---

## POST Request Method (Basic)

### Initial Implementation

```python
from fastapi import FastAPI, Body

@app.post("/create-book")
async def create_book(book_request = Body()):
    books.append(book_request)

```

### Problems with Basic Implementation

- **No Validation**: Accepts any data format
- **No Type Checking**: Can receive invalid data types
- **No Field Constraints**: Allows negative IDs, extreme ratings

---

## Data Validation with Pydantic

### What is Pydantic?

- **Purpose**: Python library for data modeling, parsing, and error handling
- **Benefits**: Efficient data validation for FastAPI applications
- **Integration**: Comes pre-installed with FastAPI

### Import Pydantic

```python
from pydantic import BaseModel, Field
from typing import Optional

```

---

## BookRequest Model

### Basic BookRequest Class

```python
class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    description: str
    rating: int

```

### ASCII Representation of Data Flow

```
Client Request → BookRequest (Validation) → Book Object → Books List

┌─────────────┐    ┌─────────────────┐    ┌─────────────┐    ┌─────────────┐
│   Client    │───→│  BookRequest    │───→│    Book     │───→│ Books List  │
│   (JSON)    │    │  (Pydantic)     │    │  (Object)   │    │ (Storage)   │
└─────────────┘    └─────────────────┘    └─────────────┘    └─────────────┘
                          ↑
                    Validation Here

```

---

## Field Validation

### Adding Field Constraints

```python
from pydantic import BaseModel, Field

class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)  # Greater than 0, less than 6 (1-5)

```

### Field Validation Rules

- **title**: Minimum 3 characters
- **author**: Minimum 1 character
- **description**: Between 1-100 characters
- **rating**: Between 1-5 (gt=0 means >0, lt=6 means <6)
- **id**: Optional field, not required for creation

---

## Improved POST Method

### Converting BookRequest to Book

```python
@app.post("/create-book")
async def create_book(book_request: BookRequest):
    # Convert BookRequest to Book object
    new_book = Book(**book_request.dict())  # or .model_dump() for Pydantic v2

    # Auto-assign ID
    new_book = find_book_id(new_book)

    # Add to books list
    books.append(new_book)

```

### Pydantic Version Differences

- **Pydantic v1**: Use `.dict()`
- **Pydantic v2**: Use `.model_dump()`

---

## Auto-ID Assignment

### ID Generation Function

```python
def find_book_id(book):
    # Ternary operator version
    book.id = 1 if len(books) == 0 else books[-1].id + 1
    return book

# Alternative if-else version:
def find_book_id(book):
    if len(books) > 0:
        book.id = books[-1].id + 1
    else:
        book.id = 1
    return book

```

### How Auto-ID Works

1. Check if books list is empty
2. If empty: assign ID = 1
3. If not empty: assign ID = last book's ID + 1

---

## Model Configuration

### Adding Example Data for Swagger UI

```python
class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "Coding with Ruby",
                "description": "A new description of a book",
                "rating": 5
            }
        }
    }

```

### Version Notes

- **New**: `model_config` with `json_schema_extra`
- **Old**: `class Config` with `schema_extra`

---

## Key Concepts Explained

### Double Asterisk Operator (\*\*)

```python
# This:
Book(**book_request.dict())

# Is equivalent to:
Book(
    id=book_request.id,
    title=book_request.title,
    author=book_request.author,
    description=book_request.description,
    rating=book_request.rating
)

```

### Optional Fields

```python
# Makes field optional in requests
id: Optional[int] = None

# With Field description
id: Optional[int] = Field(description="ID is not needed on create", default=None)

```

---

## Complete Working Code Structure

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

# Book class (data storage)
class Book:
    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

# BookRequest class (validation)
class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "Coding with Ruby",
                "description": "A new description of a book",
                "rating": 5
            }
        }
    }

# Initialize books list
books = [
    Book(1, "Computer Science Pro", "Coding with Ruby", "A very nice book", 5),
    # ... more books
]

# Helper function
def find_book_id(book):
    book.id = 1 if len(books) == 0 else books[-1].id + 1
    return book

# API Endpoints
@app.get("/books")
async def read_all_books():
    return books

@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())  # or .dict() for v1
    new_book = find_book_id(new_book)
    books.append(new_book)

```

---

## Error Handling

### Validation Errors

When validation fails, FastAPI automatically returns:

- **Status Code**: 422 (Unprocessable Entity)
- **Error Message**: Specific validation error details

### Example Error Response

```json
{
  "detail": [
    {
      "loc": ["body", "rating"],
      "msg": "ensure this value is greater than 0",
      "type": "value_error.number.not_gt",
      "ctx": { "limit_value": 0 }
    }
  ]
}
```

---

## Testing with Swagger UI

### Access Swagger Documentation

- **URL**: `http://localhost:8000/docs`
- **Features**: Interactive API testing, schema viewing, example requests

### Testing Steps

1. Navigate to `/docs`
2. Expand the endpoint you want to test
3. Click "Try it out"
4. Fill in the request data
5. Click "Execute"
6. View the response

---

## Summary of Key Benefits

1. **Type Safety**: Pydantic ensures correct data types
2. **Validation**: Field constraints prevent invalid data
3. **Documentation**: Auto-generated Swagger docs with examples
4. **Error Handling**: Clear validation error messages
5. **Separation of Concerns**: BookRequest for validation, Book for storage
6. **Professional Structure**: Follows FastAPI best practices

This foundation prepares you for implementing PUT and DELETE operations while maintaining data integrity and providing excellent developer experience.

# —-

## Table of Contents

![image.png](attachment:be0f01e8-02ca-48c5-8d50-2b2c0c7746fd:image.png)

## Getting Book by ID

### Purpose

Create an API endpoint to find a specific book using its unique ID.

### Implementation

```python
@app.get("/books/{book_id}")
async def read_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book

```

### How it Works

- **Path Parameter**: `{book_id}` captures the ID from the URL
- **Loop Through Books**: Searches through all books in the list
- **Match Found**: Returns the book when IDs match
- **No Match**: Returns nothing (will be improved later with exceptions)

### Example Usage

- URL: `/books/4`
- Response: Returns book with ID 4 containing title, author, description, and rating

---

## Filtering Books by Rating

### Purpose

Create an endpoint to get all books with a specific rating using query parameters.

### Implementation

```python
@app.get("/books/")
async def read_book_by_rating(book_rating: int):
    books_to_return = []
    for book in books:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

```

### Key Concepts

- **Query Parameter**: `book_rating` is passed as `?book_rating=5`
- **Empty List**: Creates a container for matching books
- **Filter Logic**: Only books with matching ratings are added
- **No URL Conflict**: Query parameters don't interfere with path parameters

### Example Usage

- URL: `/books/?book_rating=5`
- Response: Returns all books with 5-star rating

---

## Updating Books (PUT Request)

### Purpose

Modify existing book data by sending updated information in the request body.

### Implementation

```python
@app.put("/books/update_book")
async def update_book(book: BookRequest):
    for i in range(len(books)):
        if books[i].id == book.id:
            books[i] = book

```

### How it Works

- **Request Body**: Accepts a `BookRequest` object with all book data
- **ID Matching**: Finds the book with the same ID
- **Replace**: Completely replaces the old book with new data
- **Optional ID**: BookRequest has optional ID field (can be None for POST, required for PUT)

### Important Notes

- Uses the same `BookRequest` model as POST
- ID is optional in the model but required for updating
- Currently doesn't handle non-existent IDs (returns 200 even if nothing updated)

---

## Deleting Books (DELETE Request)

### Purpose

Remove a book from the collection using its ID.

### Implementation

```python
@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    for i in range(len(books)):
        if books[i].id == book_id:
            books.pop(i)
            break

```

### How it Works

- **Path Parameter**: Book ID from URL
- **Find Index**: Loops through books to find matching ID
- **Remove**: Uses `pop(i)` to remove book at index `i`
- **Break**: Exits loop after deletion to prevent errors

### Visual Representation

```
Before: [Book1, Book2, Book3, Book4]
Delete Book2: books.pop(1)
After:  [Book1, Book3, Book4]

```

---

## Adding Published Date Field

### Assignment Solution

### 1. Update Book Class

```python
class Book:
    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

```

### 2. Update BookRequest Class

```python
class BookRequest(BaseModel):
    # ... other fields ...
    published_date: int = Field(gt=1999, lt=2031)

    class Config:
        schema_extra = {
            # ... other fields ...
            "published_date": 2029
        }

```

### 3. Update Existing Books

Add published dates to all existing books in the books list:

```python
books = [
    Book(1, "Title 1", "Author 1", "Description 1", 5, 2030),
    Book(2, "Title 2", "Author 2", "Description 2", 4, 2030),
    # ... more books with dates
]

```

### 4. Create Filter Endpoint

```python
@app.get("/books/publish/")
async def read_book_by_publish_date(published_date: int):
    books_to_return = []
    for book in books:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return

```

### Field Validation

- **Range Check**: Published date must be between 1999 and 2031
- **Automatic Validation**: Pydantic automatically validates the field
- **Error Response**: Returns validation error if date is outside range

---

## Path Parameter Validation

### Purpose

Add validation rules to URL path parameters to ensure they meet specific criteria.

### Implementation

```python
from fastapi import FastAPI, Path

@app.get("/books/{book_id}")
async def read_book(book_id: int = Path(gt=0)):
    # ... function body

```

### How it Works

- **Import Path**: Import `Path` from FastAPI
- **Validation Rule**: `gt=0` means "greater than 0"
- **Automatic Check**: FastAPI validates before running the function
- **Error Response**: Returns 422 status code if validation fails

### Example Validation Rules

- `gt=0`: Greater than 0
- `lt=100`: Less than 100
- `ge=1`: Greater than or equal to 1
- `le=10`: Less than or equal to 10

### Error Response Example

```json
{
  "detail": [
    {
      "msg": "ensure this value is greater than 0",
      "type": "value_error"
    }
  ]
}
```

---

## Query Parameter Validation

### Purpose

Add validation to query parameters (like rating and published_date filters).

### Implementation

```python
from fastapi import FastAPI, Path, Query

@app.get("/books/")
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    # ... function body

@app.get("/books/publish/")
async def read_book_by_publish_date(published_date: int = Query(gt=1999, lt=2031)):
    # ... function body

```

### Validation Rules Applied

- **Rating**: Must be between 1 and 5 (gt=0, lt=6)
- **Published Date**: Must be between 1999 and 2031
- **Consistent Rules**: Same validation as in the BookRequest model

### Benefits

- **Input Validation**: Prevents invalid queries before processing
- **Consistent Rules**: Matches the validation in data models
- **Clear Error Messages**: Users understand what went wrong

---

## HTTP Status Codes

### Overview

HTTP status codes tell clients what happened with their request.

### Status Code Categories

### 2xx - Success

- **200 OK**: Standard successful response (GET requests)
- **201 Created**: Successfully created new resource (POST requests)
- **204 No Content**: Success but no data returned (PUT/DELETE requests)

### 4xx - Client Errors

- **400 Bad Request**: Invalid request format
- **401 Unauthorized**: Authentication required
- **404 Not Found**: Resource doesn't exist
- **422 Unprocessable Entity**: Validation errors

### 5xx - Server Errors

- **500 Internal Server Error**: Something went wrong on the server

### Visual Status Code Guide

```
┌─────────────────────────────────────┐
│           HTTP Status Codes         │
├─────────────────────────────────────┤
│ 2xx SUCCESS                         │
│ ├─ 200 OK (Data returned)           │
│ ├─ 201 Created (New resource)       │
│ └─ 204 No Content (Success, no data)│
│                                     │
│ 4xx CLIENT ERROR                    │
│ ├─ 400 Bad Request                  │
│ ├─ 404 Not Found                    │
│ └─ 422 Validation Error             │
│                                     │
│ 5xx SERVER ERROR                    │
│ └─ 500 Internal Server Error        │
└─────────────────────────────────────┘

```

---

## HTTP Exceptions

### Purpose

Handle cases where valid input doesn't match any data (like requesting a non-existent book).

### Implementation

```python
from fastapi import FastAPI, HTTPException

@app.get("/books/{book_id}")
async def read_book(book_id: int = Path(gt=0)):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found")

```

### Enhanced PUT Method

```python
@app.put("/books/update_book")
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(books)):
        if books[i].id == book.id:
            books[i] = book
            book_changed = True

    if not book_changed:
        raise HTTPException(status_code=404, detail="Item not found")

```

### How it Works

- **Validation First**: Path/query validation happens before the function runs
- **Business Logic Check**: Function checks if the requested item exists
- **Raise Exception**: If item not found, raise HTTPException
- **Automatic Response**: FastAPI converts exception to proper HTTP response

### Exception Flow

```
Request → Validation → Function Logic → Exception Check → Response
    ↓         ↓            ↓              ↓           ↓
   Valid?   Pass?      Found?        Raise?      Status

```

---

## Custom Status Code Responses

### Purpose

Explicitly set appropriate status codes for successful operations instead of defaulting to 200.

### Implementation

```python
from starlette import status

# GET requests - return data
@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return books

# POST requests - create new resource
@app.post("/books/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    # ... create logic

# PUT requests - update, no data returned
@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    # ... update logic

# DELETE requests - remove, no data returned
@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    # ... delete logic

```

### Status Code Guidelines

### When to Use Each Code

- **200 OK**: GET requests that return data
- **201 Created**: POST requests that create new resources
- **204 No Content**: PUT/DELETE requests that don't return data

### Benefits

- **Professional API**: Proper status codes make APIs more professional
- **Clear Communication**: Clients know exactly what happened
- **Standard Compliance**: Follows HTTP standards

### Complete API Structure

```
GET    /books              → 200 OK (returns all books)
GET    /books/{id}         → 200 OK (returns one book)
GET    /books/?rating=5    → 200 OK (returns filtered books)
POST   /books/create-book  → 201 Created (creates new book)
PUT    /books/update_book  → 204 No Content (updates book)
DELETE /books/{id}         → 204 No Content (deletes book)

```

---

## Complete API Architecture

### Request/Response Flow

```
┌──────────────┐    ┌─────────────────┐    ┌──────────────┐
│    CLIENT    │────│   VALIDATION    │────│   FUNCTION   │
│   (Browser)  │    │ Path/Query/Body │    │    Logic     │
└──────────────┘    └─────────────────┘    └──────────────┘
        │                     │                     │
        │                     ▼                     │
        │            ┌─────────────────┐            │
        │            │ Error Response  │            │
        │            │ (422, 400, etc) │            │
        │            └─────────────────┘            │
        │                                           │
        │                     ┌──────────────┐     │
        └─────────────────────│   RESPONSE   │─────┘
                              │ Status + Data│
                              └──────────────┘

```

### Key Features Implemented

- ✅ **CRUD Operations**: Create, Read, Update, Delete
- ✅ **Data Validation**: Pydantic models with field validation
- ✅ **Parameter Validation**: Path and query parameter validation
- ✅ **Error Handling**: HTTP exceptions for missing resources
- ✅ **Status Codes**: Proper HTTP status codes for all operations
- ✅ **Professional API**: Industry-standard practices

This complete system provides a robust foundation for building FastAPI applications with proper validation, error handling, and HTTP compliance.
