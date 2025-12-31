# Python core
## Unpacking
### `Todos(**{...})` — ultra-short recap

- `**` means *keyword argument unpacking*
- A dictionary is expanded into named constructor arguments

### Example
```python
Todos(**{"title": "Buy milk", "priority": 3})
```

is equivalent to:

```python
Todos(title="Buy milk", priority=3)
```




- `todo_request.dict()` (or `model_dump()` in Pydantic v2) returns the dictionary
- `SQLAlchemy` accepts keyword arguments matching column names
- If a key does **not** match a column → `TypeError`

One-sentence summary:  
`Todos(**data)` creates an ORM object by mapping dict keys to constructor arguments.
