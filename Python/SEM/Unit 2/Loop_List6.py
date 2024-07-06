#FOR LOOP
#Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
print()

#Use the range() and len() functions to create a suitable iterable.
#Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
print()

#WHILE LOOP
#Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
#Remember to increase the index by 1 after each iteration.
#Print all items, using a while loop to go through all the index numbers
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
print()

#LOOP COMPREHENSION
#List Comprehension offers the shortest syntax for looping through lists:
#A short hand for loop that will print all items in a list:
#Also solve expressions in loop comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
print()
