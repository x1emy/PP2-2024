#ex1
print("Hello")
print('Hello')
#ex2
a = "Hello"
print(a)
#ex3 Multiline
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#or
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#ex4 strings are arrays get the character  at position 1
a = "Hello, World!"
print(a[1])
#ex5 loop
for x in "banana":
  print(x)
#ex6 length
a = "Hello, World!"
print(len(a))
#ex7 check string
txt = "The best things in life are free!"
print("free" in txt)
#or
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
#ex8 check if not
txt = "The best things in life are free!"
print("expensive" not in txt)
#or
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

######Sclinig strings
b = "Hello, World!"
print(b[2:5]) #output llo

b = "Hello, World!"
print(b[:5]) #output hello

b = "Hello, World!"
print(b[2:])

b = "Hello, World!" 
print(b[-5:-2]) 

#######Modify strings
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

####STrings concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#####String Format
age = 36
txt = "My name is John, I am " + age
print(txt)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#####Escape Characters
txt = "We are the so-called \"Vikings\" from the north."


