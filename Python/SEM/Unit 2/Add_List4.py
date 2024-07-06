#append - method (at last)
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
print()

#insert - method (specific position)
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
print()

#extend - method (currebt list + another list)
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
print()

#extend - method
#we can extend any obj like tuples,dictionaries and sets
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)