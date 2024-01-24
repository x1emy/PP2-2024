#ex 1
def myfunc():
    global x
    x="fantastic"
#ex 2
x=5
print(type(x))
#answer:  int

#ex3
x=20.5
print(type(x))
#answer:  float

#ex 4
x=["apple","banana","cherry"]
print(type(x))
#answer:  list

#ex 5
x=("apple","banana","cherry")
print(type(x))
#answer:  tuple

#ex 6
x={"name" : "John", "age" : 36}
print(type(x))
#answer:  dict

#ex7
x=True
print(type(x))
#answer: bool