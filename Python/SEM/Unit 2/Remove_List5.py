#remove - method (specific item)
#Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
print()

#Remove the first occurrence of "banana":
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
print()

#pop - method (specific index)
#Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
print()

#Remove the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
print()

#del - keyword
#Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
print()

#Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist
print()

#clear - method (complete)
#Clear the list content:
#The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)