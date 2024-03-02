import os

path = input("Enter path: ")
if os.path.exists(path):
    print("given path exists")
    if os.path.isfile(path):
        os.remove(path)
        print("file wad deleted")
    elif os.path.isdir(path):
        os.rmdir(path)
        print("dir  was deleted")
else:
    print("does not exists")
