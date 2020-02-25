import os
import sys
import datetime

old_days = 3 # number of days for deletion of older files

path = input("Enter the directory path :")
if not os.path.exists(path):
    print("Invalid directory path")
    sys.exit(100)
if os.path.isfile(path):
    print("Please enter some directory path")
    sys.exit(101)
today = datetime.datetime.now()
files_list = os.listdir(path)
for each in files_list:
    eachpath = os.path.join(path,each)
    print (f"Created date for {each} is before \t" + str(today-datetime.datetime.fromtimestamp(os.path.getmtime(eachpath))))
