import random
value=random.randint(1,20)
print(value)
username=str(input("Hello! What is your name: "+"\n"))
def guess(value):
    cnt= 0
    print("Well, " + username + ", I am thinking of a number between 1 and 20."+ "\n" + "Take a guess.")
    while True:
        num=int(input())
        cnt+=1
        if value>num:
            print("Your guess is too low." + "\n"+"Take a guess." )
        elif value<num:
            print("Your guess is too high." + "\n"+ "Take a guess." )
        elif value==num:
            print("Good job, "+username+"! "+"You guessed my number in "+str(cnt)+" guesses!")
            break
(guess(value))

