n=int(input("Enter the number: "))
def iterate(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i
for i in iterate(n):
    print (i)