import re
with open("row.txt") as file:
    word=file.read()
pattern=r'[ ,.]'
print(re.sub(pattern,":",word))