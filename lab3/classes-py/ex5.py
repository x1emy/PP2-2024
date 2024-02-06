class Account():
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,money):
        self.balance+=money
        print("Hi dear", self.owner, "!", "Your balance now is: ", self.balance)
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            print("Now your balance now: ", self.balance)
        else:
            print("You do not have enough money!!!")
bank=Account(input("Enter your name: "))
bank.deposit(int(input("Enter the amount of money you want to input: ")))
bank.withdraw(int(input("Enter the amount of money you to withdraw: ")))

