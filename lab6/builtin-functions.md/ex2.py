str1=input("Enter your string: ")
up_l=0
lw_l=0
for i in str1:
    if i.isupper():
        up_l+=1
    if i.islower():
        lw_l+=1
print("The number of upcase letters: ",up_l, "\n", "The number of lowcase letters: ",lw_l)