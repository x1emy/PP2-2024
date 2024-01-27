#example 1 #print all keys
for x in thisdict:
  print(x)

#example 2 #print all values
for x in thisdict:
  print(thisdict[x])
#example 3
for x in thisdict.values():
  print(x)

#example 4
for x in thisdict.keys():
  print(x)

#example 5 #both keys and values its items
for x, y in thisdict.items():
  print(x, y)