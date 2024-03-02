with open("copy1.txt","r") as copy1, open("copy2.txt", "w") as copy2:
    for i in copy1:
        copy2.write(i)