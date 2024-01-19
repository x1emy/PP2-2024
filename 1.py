x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc()
a= "awesome"
print("\n")
def myfunc2():
    a="fantastic"
    print("Python is " + a)
myfunc2()
print("Python is " + a)
print("\n")
#The Global Keyword
def myfunc3():
    global c
    c = "fantastic"
myfunc3()
print("Python is " + c)
print("\n")
t = "awesome"
def myfunc4():
    global t 
    t = "fantastic"
myfunc4()
print("Python is " + t)