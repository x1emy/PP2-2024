#example 1
thislist = ["apple", "banana", "cherry"]
print(thislist)

#example 2
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#example 3
###LIST LENGTH START WITH 1 not 0
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#example 4
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#example 5
list1 = ["abc", 34, True, 40, "male"]

#example 6
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#example 7
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

"""
1)List is a collection which is ordered and changeable. Allows duplicate members.
2)Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
3)Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
4)Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove and/or add items whenever you like.
"""