#example 1
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#example 2
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#example 3
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#example 4
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#example 5
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)