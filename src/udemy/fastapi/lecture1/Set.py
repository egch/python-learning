#no duplicates
my_set = {1,2,3,4,5,1}


print(my_set) #{1, 2, 3, 4, 5}
print(len(my_set)) #5

# order is not guaranteed
for x in my_set:
    print(x)
## error
#print(my_set[0])
# remove the element 3 from the set, not the 3rd element
my_set.discard(3)

print(my_set) #{1, 2, 4, 5}
# remove all the elements
my_set.clear()
print(my_set)  #set()