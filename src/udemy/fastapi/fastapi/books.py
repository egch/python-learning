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


# The order of api top-down matters!
@app.get("/")
async def first_api():
#def first_api():
    return {"message": "Hello Enrico"}


@app.get("/books")
async def read_all_books():
    return  BOOKS

#########################################
######### Path Parameters ##############
#########################################
@app.get("/books/title/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book

# it's important to specify the type in this case

@app.get("/books/{dynamic_param}")
async def read_all_books(dynamic_param: int):
    return BOOKS[dynamic_param]

#########################################
######### Query Parameters ##############
#########################################


