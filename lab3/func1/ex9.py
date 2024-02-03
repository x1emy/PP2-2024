def volume(r):
    v=4/3 * 3.14*r**3
    return v
r=int(input("Enter radius: "))
print("The volume of sphere: ", volume(r))