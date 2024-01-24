#example 1
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#example 2
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#example 3 THE 5th ELEM IS NOT INCLUDED
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#example 4 the 4th elem is not included
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#example 5
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#example 6 #-1 is not included
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#example 7
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")