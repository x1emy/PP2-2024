import re
with open("row.txt") as file:
    word=file.read()
print(re.findall("a.*bb",word))