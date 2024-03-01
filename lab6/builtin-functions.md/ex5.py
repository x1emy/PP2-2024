n = input("Enter elems: ")
mytuple = tuple(bool(int(elem)) for elem in n.split())
print(all(mytuple))
