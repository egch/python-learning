
# Assignment
# 1. Create a new API Endpoint that can fetch all books from a specific author using either Path Parameters
# or Query Parameters.
#
from fastapi import FastAPI


app = FastAPI()

BOOKS =[
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}

]




@app.get("/books")
async def read_all_books():
    return  BOOKS


@app.get("/books/author/{author}")
async def read_book(book_author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold():
            books_to_return.append(book)
    return books_to_return
