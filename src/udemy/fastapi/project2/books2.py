from selectors import SelectSelector
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

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


# adding some validation
class BookRequest(BaseModel):
    id: Optional[int] = Field(description='ID is not needed on create', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=60)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Clean Code",
                "author": "Robert C. Martin",
                "description": "A book about writing clean, maintainable code",
                "rating": 10
            }
        }
    }


BOOKS = [
    Book(1, "Computer Science", "Enrico Giurin",
         "A concise introduction to core computer science concepts", 5),

    Book(2, "Vocabulary", "Enrico Giurin",
         "An overview of the tech stack behind the Vocabulary app", 4),

    Book(3, "The Pragmatic Programmer", "Andrew Hunt & David Thomas",
         "Practical advice for modern software development", 4),

    Book(4, "Design Patterns", "Erich Gamma et al.",
         "Elements of reusable object-oriented software", 4),

    Book(5, "Refactoring", "Martin Fowler",
         "Improving the design of existing code", 4),

    Book(6, "Java in Practice", "Enrico Giurin",
         "Practical examples and best practices for modern Java development", 5),
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book

# TO BE COMPLETED
@app.get("/books/")
async def read_book_by_rating(book_rating: int):
    books_to_return = []


@app.post("/create_book")
async def create_book(book_request: BookRequest):
    # converting the request to Book object
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))


# we want to increase the id
# BOOKS[-1] -> return the last element of the collection
def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book
