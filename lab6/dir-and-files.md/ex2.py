import os

path=input("Enter path: ")
print("exist: ",os.access(path, os.F_OK)) #existance
print("readable: ",os.access(path, os.R_OK)) #readable
print("writable: ",os.access(path, os.W_OK)) #writability
print("exucutable: ",os.access(path,os.X_OK)) #exucutable