from fastapi import FastAPI, Body


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

@app.get("/books/")
async def react_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# path parameter & query parameter combined
@app.get("/books/author/{author}")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold() and \
            book.get("author").casefold() == book_author.casefold():
                books_to_return.append(book)
    return books_to_return


#########################################
#########     POST HTTP    ##############
#########################################

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

#########################################
#########     PUT HTTP    ###############
#########################################

# This is a wrong way to run a PUT (update). We should go restful having an id to uniquely identify the element
# of the collection to be updated
@app.put("/books/update_book")
async def update_book(update_book=Body()):
    for index in range(len(BOOKS)):
        if BOOKS[index].get('title').casefold() == update_book.get('title').casefold():
            BOOKS[index].update(update_book)


#########################################
#########     DELETE HTTP    ############
#########################################
@app.delete("/books/")
async def delete_book(book_tile: str):
    for index in range(len(BOOKS)):
        if BOOKS[index].get("title").casefold() == book_tile.casefold():
            BOOKS.pop(index)
            break


