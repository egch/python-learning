"""
String Assignment. (This can be tricky so feel free to watch solution so we can do it together)

- Ask the user how many days until their birthday

- Using the print()function. Print an approx. number of weeks until their birthday

- 1 week is = to 7 days.
"""


# it fails if we do not call int()
days = int(input("how many days to your bd: "))
num_of_weeks = days / 7


print(num_of_weeks)
print(round(days/7, 2))  # 3.29


