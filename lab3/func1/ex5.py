import itertools #library for iterations переборы и тд
user=str(input("Enter the string: "))
def permutations(user):
    for i  in itertools.permutations(user):
        a=''.join(i) #join all items to a string
        print(a)
permutations(user)
