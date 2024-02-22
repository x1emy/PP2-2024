import re

with open("forex8.txt") as file:
    word = file.read()
print(re.findall(r"[A-Z][^A-Z]*",word))