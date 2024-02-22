import re
with open("forex7.txt") as file:
    word=file.read()
print(re.sub(r"_","",word))
