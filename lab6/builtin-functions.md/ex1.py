# Write a Python program with builtin function to multiply all the numbers in a list
n=input("Enter numbers: ")
mylist=[]
for i in n.split():
    num=int(i)
    mylist.append(num)
x=iter(mylist)
multiply=1
for i in mylist:
    multiply*=next(x)
print(multiply)