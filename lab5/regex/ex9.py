import re
with open("forex9.txt") as file:
    word = file.read()
find=re.findall(r'[A-Z][a-z]*',word) #ЗАГЛАВНЫЕ БУКВУ ПОТОМ ОСТАЛЬНОЕ
print(' '.join(find)) #все в одну строку