# FastAPI Books Project - Complete Notes

## Project Overview

### What We're Building

- A Books API using FastAPI
- Learn basic HTTP request methods
- Implement CRUD operations (Create, Read, Update, Delete)

### Book Structure

Each book has three properties:

- **Title**: Title One, Title Two, etc.
- **Author**: Author One, Author Two, etc.
- **Category**: Science, History, Math

### HTTP Request Methods & CRUD

```
CREATE  → POST
READ    → GET
UPDATE  → PUT
DELETE  → DELETE

```

### Request/Response Flow

```
Web Page  ──request──→  FastAPI Server
          ←─response─←

```

## Setting Up FastAPI

## Environment Setup

### Step-by-Step Installation (Windows)

bash

`_# 1. Create a project folder_
mkdir fastapi #any name i set the name 02. Books Proejct

_# 2. Navigate to the project folder_
cd fastapi

_# 3. Create a virtual environment_
python -m venv fastapienv

_# 4. Check if virtual environment was created_
dir

_# 5. Activate the virtual environment (Windows)_
fastapienv\Scripts\activate.bat

_# 6. Check installed packages (optional)_
pip list

_# 7. Install FastAPI_
pip install fastapi

_# 8. Install Uvicorn server_
pip install "uvicorn[standard]"

_# 9. Deactivate when done working_
deactivate`

### File Structure

`fastapi/
├── fastapienv/          # Virtual environment folder
├── books.py             # Main application file
└── other_files...`

### 1. Project Setup

- Create virtual environment
- Install FastAPI
- Create `books.py` file

### 2. Basic FastAPI Structure

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def first_api():
    return {"message": "Hello, Devaza"}

```

### 3. Running the Application

Two methods:

**Method 1: Using Uvicorn**

```bash
uvicorn books:app --reload

```

**Method 2: Using FastAPI CLI (newer versions)**

```bash
fastapi run books.py
# or for development mode
fastapi dev books.py

```

### 4. Accessing the Application

- Main URL: `http://127.0.0.1:8000`
- Swagger UI: `http://127.0.0.1:8000/docs`

## Creating the Books Data

### Sample Books List

```python
BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Two", "category": "math"}
]

```

### Get All Books Endpoint

```python
@app.get("/books")
async def read_all_books():
    return BOOKS

```

## Path Parameters

### What Are Path Parameters?

- Dynamic parts of the URL
- Used to identify specific resources
- Defined with curly braces `{}`

### URL Structure

```
Static:   /books
Dynamic:  /books/{book_title}

```

### Example Implementation

```python
@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

```

### Important Notes

- **Order Matters**: Static paths must come before dynamic ones
- **Type Specification**: Use `: str`, `: int`, etc.
- **URL Encoding**: Spaces become `%20` in URLs

### Path Parameter Order Example

```python
# CORRECT ORDER
@app.get("/books/my-book")  # Static - comes first
async def read_favorite_book():
    return {"book_title": "My Favorite Book"}

@app.get("/books/{dynamic_param}")  # Dynamic - comes second
async def read_book_dynamic(dynamic_param: str):
    return {"dynamic_param": dynamic_param}

```

## Query Parameters

### What Are Query Parameters?

- Filter data using URL parameters
- Come after `?` in the URL
- Format: `?parameter=value`

### URL Structure

```
Basic Query:     /books?category=science
Multiple Query:  /books?category=science&author=Author%20One

```

### Example Implementation

```python
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

```

## Combining Path and Query Parameters

### Mixed Parameters Example

```python
@app.get("/books/{book_author}")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (book.get('author').casefold() == book_author.casefold() and
            book.get('category').casefold() == category.casefold()):
            books_to_return.append(book)
    return books_to_return

```

### URL Example

```
/books/Author%20Two?category=science

```

## Key FastAPI Features

### Swagger UI

- Automatic API documentation
- Interactive testing interface
- Access at `/docs` endpoint

### Async Functions

- `async def` is optional but recommended
- FastAPI handles async automatically

### Type Hints

- Specify parameter types: `str`, `int`, etc.
- Enables automatic validation

## Visual Representation

### API Endpoint Structure

```
FastAPI Application
├── GET /books
│   └── Returns all books
├── GET /books/{book_title}
│   └── Returns specific book by title
├── GET /books/?category={category}
│   └── Returns books filtered by category
└── GET /books/{author}?category={category}
    └── Returns books by author and category

```

### HTTP Request Flow

```
Client Request:  GET /books/Title%20One
                      ↓
FastAPI Router:  Matches /books/{book_title}
                      ↓
Function Call:   read_book(book_title="Title One")
                      ↓
Response:        {"title": "Title One", "author": "Author One", "category": "science"}

```

## Common Patterns

### String Comparison Best Practice

```python
# Use casefold() for case-insensitive comparison
if book.get('title').casefold() == book_title.casefold():
    return book

```

### Multi-line Conditions

```python
# Use backslash for line continuation
if (book.get('author').casefold() == book_author.casefold() and \
    book.get('category').casefold() == category.casefold()):
    books_to_return.append(book)

```

## Next Steps

This covers the GET (Read) operations. The course continues with:

- POST (Create) operations
- PUT (Update) operations
- DELETE operations
- Data validation
- Error handling
