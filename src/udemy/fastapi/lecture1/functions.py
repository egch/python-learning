"""
Functions
"""

def my_function():
    print("inside my_function()")

def print_my_name(name):
    print(f"Hello {name}")

print_my_name("enrico")  #Hello enrico

def print_numbers(lowest=3, highest=5):
    print(lowest)
    print(highest)


print_numbers() # 3, 5
print_numbers(10, 20) #10, 20


def multiply_numbers(a,b):
    return a * b

solution = multiply_numbers(3,4)
print(solution) # 124

def print_list(list_of_numbers):
    for x in list_of_numbers:
        print(x)

list_of_numbers = [1, 2, 3, 4, 5]
print_list(list_of_numbers)

"""
call another Function
"""
def buy_item(cost_of_item):
    return cost_of_item + add_cost_to_item(cost_of_item)

def add_cost_to_item(cost_of_item):
    current_tax_rate = 0.3
    return cost_of_item * current_tax_rate

final_cost = buy_item(21)
print(final_cost) # 27.3