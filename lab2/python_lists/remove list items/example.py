#example 1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#example 2
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#example 3 starts with 0
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#example 4 remove last elem
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#example 5
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#example 6
thislist = ["apple", "banana", "cherry"]
del thislist

#example 7 #empties list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)



