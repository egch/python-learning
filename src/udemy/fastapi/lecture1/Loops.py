"""
for & While Loops
"""

my_list = [1,2,3,4,5]

for element in my_list:
    print(element)


sum = 0
for x in my_list:
    sum += x

print(sum)  # 15


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in days:
    print(f"Happy {day}!")

#### while
index = 0
while index <= 5:
    print(index)
    index +=1
else:
    print("out of the while")

"""
break
"""

index = 0
while index < 100:
    index +=1
    if index == 3:
        continue
    if index == 5:
        break
    print(index)
# 1
# 2
# 4