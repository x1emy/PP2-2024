n=int(input("Enter the number: "))
def down(n):
    while n>=0:
        yield n
        n-=1
for i in down(n):
    print(i)