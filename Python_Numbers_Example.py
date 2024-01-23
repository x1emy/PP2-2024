#ex1
x=1
y=2.8
z=1j
#ex2
print(type(x))
print(type(y))
print(type(z))
#ex3 INT
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
#ex 4 FLOAT
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
#ex 5 FLOATS
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
#ex 6 COMPLEX
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
#ex 7 TYPE CONVERSION
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
#ex8 random number
import random

print(random.randrange(1, 10))