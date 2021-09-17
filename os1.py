import os
import shutil
import sys
import platform

# print(os.name)
# print(sys.platform)
# print(platform.system())

var = os.walk("/opt/homebrew/etc/")

print(var)

#os.rename("api.psy","api.py") #renaming a file

#print(os.listdir("/Users/shourjadeepdatta/Desktop/Python/Zomato")) #listing all the files in the specified path

#print(os.getcwd()) # current working directory

# for file in os.listdir():    # for printing a particular type of a file
#     if file.startswith("a"):
#         print(file)

#os.makedirs("hello\intel") # creating a directory

#os.remove("/Users/shourjadeepdatta/Desktop/Python/file1.py") # removing a particular file

#shutil.copyfile("Ali.py","/Users/shourjadeepdatta/Desktop/Python/College/sample.py") # copying a file to another file

#shutil.move("user privileges.rtf","/Users/shourjadeepdatta/Desktop/Python/College") # moving a file to some other location