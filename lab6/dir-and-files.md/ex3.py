import os

path=input("Enter path: ")
if os.access(path,os.F_OK):
    print("given path exists")
    print("filename: ",os.path.basename(path))
    print("dirname: ",os.path.dirname(path))
else:
    print("does not exists")