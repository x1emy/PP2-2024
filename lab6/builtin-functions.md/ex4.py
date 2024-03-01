from math import sqrt
from time import sleep
n=int(input("Enter number: "))
t=int(input("Enter milliseconds: "))
sleep(t/1000)
print("Square root of ",n, "after ",t,"miliseconds is ",sqrt(n))