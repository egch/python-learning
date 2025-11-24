"""
string formatting
"""
first_name = 'enrico'
print('hi ' + first_name)

print(f"Hi {first_name}")  #interpolation

sentence = 'Hi {}'
print(sentence.format(first_name))

first_name = 'Enrico'
last_name = 'Giurin'
sentence = 'Hi {} {}'
print(sentence.format(first_name, last_name))