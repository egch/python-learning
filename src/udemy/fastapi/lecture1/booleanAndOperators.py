"""
Boolean & Operators
"""
like_coffee = True
like_tee = False

print(type(like_coffee))  # <class 'bool'>
# Comparison Operators
print(1 == 2)  # False
print(1 != 2)  # True
print(1 < 2)  # True
print(1 > 2)  # False

# Logical Operators
print(1 > 3 and 5 < 7)  # False
print(1 > 3 or 5 < 7)  # True
print(not(1 == 1))  # False

"""
If
"""

x = 2
if x == 1:
    print("x is 1")
else:
    print("x is not 1")


print("outside")


hour = 20

if hour < 15:
    print("good morning")
elif hour < 20:
    print("good afternoon")
else:
    print("good nite")
