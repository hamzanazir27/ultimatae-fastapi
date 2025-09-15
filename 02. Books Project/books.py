'''
# Practice ------------------------------------------------------<<<<<<<------------------|||
from fastapi import FastAPI, Body

app= FastAPI()



BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three","author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Two", "category": "math"}
]


@app.get("/")
async def fast_api():
    return {"message":"hello Hamza"}


@app.get("/books")
async def read_books():
    return BOOKS



# CORRECT ORDER
@app.get("/books/my-book")  # Static - comes first
async def read_favorite_book():
    return {"book_title": "My Favorite Book"}




@app.get("/books/{dynamic_param}")  # Dynamic - comes second
async def read_book_dynamic(dynamic_param: str):
    return {"dynamic_param": dynamic_param}




@app.get("/books/{book_title}")
async def fast_api(book_title:str):   #str means books title should be string if pass integer then it convert to string
    for book in BOOKS:
        if book.get("title").casefold()==book_title.casefold():
            return book
    return {"message":"not found"}




# Querry Parameter
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return
 

@app.get("/books/{book_author}")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (book.get('author').casefold() == book_author.casefold() and
            book.get('category').casefold() == category.casefold()):
            books_to_return.append(book)
    return books_to_return


# post erequest


@app.post("/books/create_book")
async def create_book(new_book = Body()):
    BOOKS.append(new_book)
    return {"message": "Book created"}


# put request
@app.put("/books/update_book")
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i]["title"].casefold() == updated_book["title"].casefold():
            BOOKS[i] = updated_book
            break
    return {"message": "Book updated"}


# delete request
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i]["title"].casefold() == book_title.casefold():
            BOOKS.pop(i)
            return {"message": "Book deleted"}
        
    return {"message": "Book Not FOund"}



'''
# Complete Application ------------------------------------------------------<<<<<<<------------------|||
from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Two", "category": "math"}
]

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Hello Hamza"}

# Get all books
@app.get("/books")
async def read_all_books():
    return BOOKS

# Static route - must come before dynamic route
@app.get("/books/my-book")
async def read_favorite_book():
    return {"book_title": "My Favorite Book"}

# Get book by title
@app.get("/books/{book_title}")
async def read_book_by_title(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book
    return {"message": "Book not found"}

# Get books by category (query parameter)
@app.get("/books/")
async def read_books_by_category(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# Get books by author and category
@app.get("/books/author/{book_author}")
async def read_books_by_author_and_category(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (book.get('author').casefold() == book_author.casefold() and
            book.get('category').casefold() == category.casefold()):
            books_to_return.append(book)
    return books_to_return

# Create new book
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return {"message": "Book created successfully"}

# Update book
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i]["title"].casefold() == updated_book["title"].casefold():
            BOOKS[i] = updated_book
            return {"message": "Book updated successfully"}
    return {"message": "Book not found"}

# Delete book
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i]["title"].casefold() == book_title.casefold():
            BOOKS.pop(i)
            return {"message": "Book deleted successfully"}
    return {"message": "Book not found"}


