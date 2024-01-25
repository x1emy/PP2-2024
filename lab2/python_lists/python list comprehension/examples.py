#example 1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#example 2
fruits=["apple", "banana","cherry","kiwi","mango"]
newlist=[]
newlist=[x for x in fruits if "a" in x]
print(newlist)

#example 3
newlist = [expression for item in iterable if condition == True]

#example 4
newlist = [x for x in fruits if x != "apple"]

#example 5
newlist = [x for x in fruits]

#example 6
newlist = [x for x in range(10)]

#example 7
newlist = [x for x in range(10) if x < 5]

#example 8
newlist = [x.upper() for x in fruits]

#example 9
newlist = ['hello' for x in fruits]

#example 10
newlist = [x if x != "banana" else "orange" for x in fruits]
