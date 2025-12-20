# Learning Python
My personal playground for learning Python.


## What is a Python virtual environment
A virtual environment is a private folder that contains its own Python interpreter and its own installed packages.

## Commands (mac)
Python Package Manager.   
pip installs external Python libraries into your environment (global or virtual environment).

```shell
p3 -m pip --version
```

Create the venv env
```shell
p3 -m venv fastapienv 
```

Activate
```shell
 source bin/activate
```

deactivate
```shell
deactivate
```

list
```shell
pip list
```

install fastapi
```shell
pip install project1 uvicorn
```

install fastapi [standard]
```shell
 pip install "fastapi[standard]"
```

### fastapi commands
```shell
uvicorn src.udemy.fastapi.project1.books:app --reload
```

### Swagger
http://127.0.0.1:8000/docs


### Queries
```shell
curl "http://127.0.0.1:8000/books/?category=science"
```
## Other HTTP Verbs
### PUT
```json
    {"title": "Title Two", "author": "Author XXX", "category": "XXX"}
```

## Pydantic
```pycon
@app.post("/books/create_book")
async def create_book(book_request: BookRequest):
    # converting the request to Book object
    new_book = Book(**book_request.dict())
    BOOKS.append(new_book)

```

## Resources


[Source](src/udemy/fastapi)

[course](https://www.udemy.com/course/fastapi-the-complete-course/)

[github project](https://github.com/codingwithroby/FastAPI-The-Complete-Course)