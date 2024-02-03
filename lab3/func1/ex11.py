def palindrom(word):
    if word[::-1]==word:
        return True
    else:
        return False
print(palindrom("madam"))
print(palindrom("abap"))
#to reverse str [::-1]