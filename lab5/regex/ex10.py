import re
with open("forex10.txt") as file:
    words=file.read()
cnt='_'
for i in words:
    if i>='A' and i<='Z':
        cnt+='_'
    cnt+=i
print(cnt)