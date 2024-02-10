import math
def area_polygon(sides,length):
    numerator=sides*(length**2)
    denominator=4*math.tan(math.pi/sides)
    print(int(numerator/denominator))
area_polygon(int(input("Input number of sides: ")), int(input("Input the length of a side: ")))