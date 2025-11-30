"""
Dictionaries

It's like a Map in Java
"""
user_dictionary = {
    'username': 'egch',
    'name': 'enrico',
    'age': 44
}
print(user_dictionary) # {'username': 'egch', 'name': 'enrico', 'age': 44}

print(user_dictionary.get("username"))   # egch
user_dictionary["married"] = True
print(user_dictionary.get("married")) #True

print(len(user_dictionary))  #4
user_dictionary.pop("age") # we remove the entry with key age
print(user_dictionary)  # {'username': 'egch', 'name': 'enrico', 'married': True}

user_dictionary.clear()  # remove the contents of the dictionary
print(user_dictionary) # {}

# declare it again
user_dictionary = {
    'username': 'egch',
    'name': 'enrico',
    'age': 44
}
for key, value in user_dictionary.items():
    print(key, value)

