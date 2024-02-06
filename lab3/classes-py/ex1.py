class ex1():
    def __init__(self):
        self.string=""
    def getString(self):
        self.string=input()
    def printString(self):
        print(self.string.upper())
string=ex1()
string.getString()
string.printString()
