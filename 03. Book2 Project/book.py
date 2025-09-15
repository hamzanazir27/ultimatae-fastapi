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
    title: str = Field(min_length=3, max_length=100)    # Increased from 12 to 100
    author: str = Field(min_length=1, max_length=50)    # Increased from 12 to 50  
    description: str = Field(min_length=1, max_length=200)  # Increased from 12 to 200
    rating: int = Field(gt=0, lt=6)  # Rating between 1-5



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
    return {"message": "Books Application"}

@app.get("/book/{book_id}")
async def read_book(book_id:int):
    for book in books:
        if (book.id==book_id):
            return book;

@app.get("/books/")
async def read_book_by_rating(book_rating: int):
    books_to_return = []
    for book in books:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

    


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



@app.put("/books/{book_id}")
async def update_book(book_id: int, book_request: BookRequest):
    for i in range(len(books)):
        if books[i].id == book_id:  # ID comes from URL
            # Convert BookRequest to Book
            updated_book = Book(**book_request.model_dump())
            updated_book.id = book_id  # Assign the ID
            books[i] = updated_book
            return {"message": "Book updated successfully"}
    return {"error": "Book not found"}



@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    for i in range(len(books)):
        if books[i].id == book_id:
            books.pop(i)
            break