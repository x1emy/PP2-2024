import os 
path=input("Write path: ")
dir_list=os.listdir(path)
print("Directories: ")
for dir in dir_list:
    print(dir)
print("\nFiles: ")
for dir in dir_list:
    if os.path.isfile(dir):
        print(dir)

