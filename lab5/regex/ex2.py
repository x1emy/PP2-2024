import re
with open("row.txt") as file:
    word=file.read()
print(re.findall("ab{0,1}",word))