n=int(input("Enter the number: "))
def even(n):
    for i in range(n+1):
        if i%2==0:
            yield i
for i in even(n):
    print(i)