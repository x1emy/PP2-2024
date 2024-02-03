mylist=[]
numbers=input("Enter numbers: ")
for i in numbers.split():
    num=int(i)
    mylist.append(num)
print(mylist)
def histogram(mylist):
    value=""
    for i in mylist:
        value+=i*"*" + "\n"
    return value
print(histogram(mylist))
