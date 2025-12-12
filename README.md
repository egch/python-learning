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
pip install fastapi uvicorn
```

### fastapi commands
```shell
uvicorn src.udemy.fastapi.fastapi.books:app --reload
```
## Resources


[Source](src/udemy/fastapi)

[course](https://www.udemy.com/course/fastapi-the-complete-course/)

[github project](https://github.com/codingwithroby/FastAPI-The-Complete-Course)