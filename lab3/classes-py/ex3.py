class Shape():
    def __init__(self,width,length):
        self.length=length
        self.width=width
class Rectangle(Shape):
    def __init__(self,width,length):
        super().__init__(width,length) #copy from previous class
    def area(self):
        print(self.width*self.length)
rect=Rectangle(int(input("enter the width: ")), int(input("enter the length: ")))
rect.area()
    
    