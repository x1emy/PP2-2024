sentence=str(input("Enter the sentence: "))
words=sentence.split()
def reverse(words):
    words.reverse()
    to_string=' '.join(words)# method how to transform from list type to str type
    print(to_string)
reverse(words)

