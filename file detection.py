import os

path = "C:\\Users\\62813\Desktop\\Code\\textfolder\\test.txt"

print(os.path.exists(path)) # True
print(os.path.isfile(path)) # True
print(os.path.isdir(path)) # False