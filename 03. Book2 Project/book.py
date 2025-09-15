from fastapi import FastAPI,Body
from pydantic import BaseModel,Field
from typing import Optional

app = FastAPI()

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


class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed on create", default=None)
    title: str =Field(min_length=0,max_length=12)
    author: str=Field(min_length=0,max_length=12)
    description: str=Field(min_length=0,max_length=12)
    rating: int =Field(gt=0,ls=12)

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



books = [
    Book(1, "Computer Science Pro", "Coding with Ruby", "A very nice book", 5),
    Book(2, "Be Fast with FastAPI", "Coding with Ruby", "This is a great book", 5),
    Book(3, "Master Endpoints", "Coding with Ruby", "This is an awesome book", 5),
    Book(4, "HP1", "Author One", "Book description", 2),
    Book(5, "HP2", "Author Two", "Book description", 3),
    Book(6, "HP3", "Author Three", "Book description", 1)
]


@app.get("/books")
async def read_all_books():
    return books

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/create-book")
async def create_book(book_request: BookRequest):
    # Convert BookRequest to Book object
    new_book = Book(**book_request.model_dump())  # or .model_dump() for Pydantic v2

    # Auto-assign ID
    new_book = find_book_id(new_book)

    # Add to books list
    books.append(new_book)

def find_book_id(book):
    # Ternary operator version
    book.id = 1 if len(books) == 0 else books[-1].id + 1
    return book