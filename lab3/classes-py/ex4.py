#Point Class - Creates a point on a coordinate plane with values x and y.
import math
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(f"x={self.x} and y={self.y}")
    def move(self,nx,ny): #newx and newy
        self.x=nx
        self.y=ny 
    def dist(self, atribute):
        dist_x=self.x-atribute.x 
        dist_y=self.y-atribute.y 
        distance=math.sqrt(dist_x**2+dist_y**2)
        return distance 
point1=Point(int(input("Enter point x1: ")),int(input("Enter point y1: ")))
point2=Point(int(input("Enter point x2: ")),int(input("Enter point y2: ")))
point1.show()
point2.show()
print("Distance = ",point1.dist(point2))
point2.move(int(input()),int(input()))
point2.show()