with open("text_forex5.txt","w") as file:
    mylist=[]
    n=input("Enter numbers: ")
    for i in n.split():
        num=int(i)
        mylist.append(num)
    print(mylist)
    file.write(str(mylist))