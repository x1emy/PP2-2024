#ex 1
class myshape():
    def __init__(self,color="red",is_filled=True):
        self.color=color
        self.is_filled=is_filled
    def __str__(self):
        filled_status="filled" if self.is_filled else "not filled"
        return f"shape color: {self.color} is {filled_status}"
    def getArea(self):
        return 0
shape1=myshape()
print(myshape("blue",False))
print(shape1,"\n", shape1.getArea())

#ex2/////////////////////////////////////////////////////////////////////////////////////////////
import math

class Rectangle(MyShape):
    def __init__(self, color="black", is_filled=True, x_top_left=0, y_top_left=0, length=0, width=0):
        super().__init__(color, is_filled)
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle: color={self.color}, is_filled={self.is_filled}, x_top_left={self.x_top_left}, y_top_left={self.y_top_left}, length={self.length}, width={self.width}"


class Circle(MyShape):
    def __init__(self, color="black", is_filled=True, x_center=0, y_center=0, radius=0):
        super().__init__(color, is_filled)
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle: color={self.color}, is_filled={self.is_filled}, x_center={self.x_center}, y_center={self.y_center}, radius={self.radius}"


# Console input for creating a rectangle
def create_rectangle():
    color = input("Enter color for the rectangle: ")
    is_filled = input("Is the rectangle filled? (True/False): ").lower() == "true"
    x_top_left = int(input("Enter x-coordinate of the top left corner: "))
    y_top_left = int(input("Enter y-coordinate of the top left corner: "))
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    return Rectangle(color, is_filled, x_top_left, y_top_left, length, width)


# Creating a rectangle and printing its details
rectangle = create_rectangle()
print(rectangle)
print("Area of the rectangle:", rectangle.getArea())
