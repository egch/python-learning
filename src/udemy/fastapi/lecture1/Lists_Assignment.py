"""
- Create a list of 5 animals called zoo

- Delete the animal at the 3rd index.

- Append a new animal at the end of the list

- Delete the animal at the beginning of the list.

- Print all the animals

- Print only the first 3 animals
"""
zoo = ['tiger', 'lion', 'cat', 'dog', 'monkey']
zoo.pop(3)
zoo.append('pinguin')
zoo.pop(0)
print(zoo)  # ['lion', 'cat', 'monkey', 'pinguin']
print(zoo[0: 3])  # ['lion', 'cat', 'monkey']
