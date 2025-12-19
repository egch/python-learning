from fastapi import FastAPI, Body

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
