n=input("enter numbers: ")
mylist=[ ]
div_by_4=[]
for i in n.split():
    num=int(i)
    mylist.append(num)
print(mylist)
for i in mylist:
    if i%4==0:
        div_by_4.append(i)
print(div_by_4)