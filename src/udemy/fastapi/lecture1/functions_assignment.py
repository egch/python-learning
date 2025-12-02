"""
Functions Assignment
- Create a function that takes in 3 parameters(firstname, lastname, age) and

returns a dictionary based on those values
"""

def person(firstname, lastname, age):
    result = {"firstname": firstname, "lastname": lastname, "age": age}
    return result

mario = person("Mario", "Rossi", 30)
print(mario) #{'firstname': 'Mario', 'lastname': 'Rossi', 'age': 30}

