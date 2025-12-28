# ToDo List
## Install dependencies

````shell
pip install sqlalchemy
````

## Running app and create db automatically
From the path of todoapp:
````shell
uvicorn main:app --reload
````

## SQLite
[link](https://sqlite.org/)

Precompiled Binaries for Windows

Windows
* Path: MySoftware\sqlite3
* exec: sqlite3

### Commands
From the path of todoapp:
```shell
todoapp>sqlite3 todos.db
```
Check the existing schema:
```shell
sqllite> .schema
```

Insert the first row
```shell
insert into todos (title, description, priority, complete) values ('Go to the store', 'Pick up eggs', 5, False);
```



