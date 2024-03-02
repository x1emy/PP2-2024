#ex 1

def calculate_factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num*calculate_factorial(num-1)
print(calculate_factorial(int(input("enter num: "))))

#ex 2
def reverse_string(str1):
    if str1==' ':
        return "empty string "
    else:
        return str1[::-1]
print(reverse_string((input("enter string: "))))

#ex 3
def get_max(a,b,c):
    return max(a,b,c)
print(get_max(int(input("enter a: ")),int(input("enter b: ")),int(input("enter c: "))))

#ex 3 if do not allow to use max()
int_max=-999
n=(input("enter number: "))
mylist=[]
for i in n.split():
    num=int(i)
    mylist.append(num)

for i in  mylist:
    if int_max<i:
        int_max=i
print(int_max)

#ex 4
def its_even(num):
    if num%2==0:
        return True
    else:
        return False
print(its_even(int(input("enter num: "))))

#ex 5
nums=input("enter numbers: ")
def filter_primes(nums):
    mylist=[]
    primes=[]
    for i in nums.split():
        num=int(i)
        mylist.append(num)
    print(mylist)
    for i in mylist:
        cnt=0
        for j in range(1,i):
            if i%j==0:
                cnt+=1
        if cnt==1:
            primes.append(i)
    return primes
print(filter_primes(nums))

#ex 6
def find_common(mylist1,mylist2):
    common=[]
    for i in mylist1:
        for j in mylist2:
            if i==j:
                common.append(i)
    return common
a=input("enter nums for list1: ")
b=input("enter nums for list2: ")
mylist1=[]
mylist2=[]
for i in a.split():
    nums=int(i)
    mylist1.append(i)
for i in b.split():
    nums=int(i)
    mylist2.append(i)
print(find_common(mylist1,mylist2))

#ex 7 #VOOBSHE NE PON
def word_frequency(str1):
    words = str1.split()
    dictionary = {}  # Changed variable name here
    for i in words:
        if i in dictionary:  # Changed variable name here
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary

str1 = input("Enter a string: ")
frequency = word_frequency(str1)
print("Word frequencies:", frequency)

#ex 8
def fibonacci(n):
    if n<=0:
        print("invalid input.")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("enter the value of n: "))
print(fibonacci(n))

#ex 9
def calculate_running(n):
    if not n:
        return []
    sumr=0
    average=[]
    for i,num in range(n,start=1):
        sumr+=n
        avg=sumr/i
        average.append(avg)
    return average
numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
averages = calculate_running_average(numbers)
print("Running averages:", averages)

