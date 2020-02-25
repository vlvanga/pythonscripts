import os
import sys

path=input("Enter the directory path: ")
if os.path.exists(path):
    filelist=os.listdir(path)
else:
    print ("Error : Please enter valid path")
    sys.exit()

file=0
directory=0
pythonfiles=0

for each in filelist:
    if os.path.isfile(os.path.join(path,each)):
        # print (os.path.join(path,each))
        file+=1
        if each.endswith(".py"):
            pythonfiles+=1
    else:
        directory+=1


print("Number of files is ",str(file))
print(f"Number of python files is {pythonfiles}")
print("Number of directories is ",str(directory))
