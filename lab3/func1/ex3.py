numheads=int(input("Enter the number of heads: "))
numlegs=int(input("Enter the number of legs: "))
def solve(numheads,numlegs):
    print("The num of chickens: ", numheads-(numlegs-numheads*2)//2, '\n', "The num of Rabbits: ", (numlegs-numheads*2)//2)
solve(numheads,numlegs)
