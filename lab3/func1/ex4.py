#list of numbers --> ouput only primes
numlist = list()
mylist=[]
n=int(input("Enter the number of lists: "))
for i in range(n):
    values = list(map(int, input("Enter the numbers separated by space: ").split()))
    numlist.append(values)
def filter_prime(numlist,mylist):
    for i in numlist:
        for j in i:
            if j%2!=0 and j%3!=0 and j%5!=0 and j%7!=0:
                if j==2:
                    continue
                if j==3:
                    continue
                if j==5:
                    continue
                if j==7:
                    continue
                mylist.append(j)
                mylist.sort()
    print(mylist)
mylist.append(2)
mylist.append(3)
mylist.append(5)
mylist.append(7)
filter_prime(numlist,mylist)

