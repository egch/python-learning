"""
Lists are a collection fo data
"""

my_list = [90, 96, 72, 100, 8]
print(my_list)

print(my_list[1])  #96
my_list.sort()
print(my_list) #[8, 72, 90, 96, 100]

people = ["Enrico", "Marco", "Giovanni"]
#print the last element of the lis
print(people[-1]) #Giovanni
print(people)
#size of list
print(len(people))
#from 0 to 2 excluded
print(people[0:2]) #['Enrico', 'Marco']
#adding Joh at the very end
people.append("John")
print(people) #['Enrico', 'Marco', 'Giovanni', 'John']
#adding Anna at the 2nd position
people.insert(2, "Anna")
print(people) #['Enrico', 'Marco', 'Anna', 'Giovanni', 'John']
