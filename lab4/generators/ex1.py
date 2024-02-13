n=int(input())
def square(n):
    for i in range(n+1):
        yield (i+1)**2
for i in square(n):
    print(i)