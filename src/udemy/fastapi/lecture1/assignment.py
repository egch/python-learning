"""
Write a Python program that can do the following:

- You have $50

- You buy an item that is $15, that has a 3% tax

- Using the print()  Print how much money you have left, after purchasing the item.

"""
initialMoney = 50
tax = 0.03
item = 15
remainingMoney = initialMoney - item - item*tax
print(remainingMoney)