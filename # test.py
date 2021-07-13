# test

# string manipulations
string = "Cumpostor"
integer = "1234"
print(len(string)) # length of the string
print(string.find("r")) # if exists
print(string.find("O")) # if doesnt exist (case-sensitive)
print(string.capitalize()) # capitalizes the first letter of a string
# print(string.capitalize("o")) will result an error bc str.capitalize() takes no arguments
print(string.upper()) # uppercases all letters
print(string.lower()) # lowercases all letters
print(string.isdigit()) # False
print(integer.isdigit()) # True
print(string.isalpha()) # is it alphabetical letters or no (A-Z)
print(integer.isalpha()) # h
print(string.count("o")) # counts how many a certain character is present in the string
# print(string.count()) takes at least one argument
print(string.replace("o","i")) # replaces old character with new ones
print(string.replace("pos","piss")) # this also works

# type casting
x = 1 # int
y = 2.0 # float
z ="3" # string

iy = int(y)
iz = int(z)
print(iy+iz)

fx = float(x)
fz = float(z)
print(fx+fz)

sx = str(x)
sy = str(y)
print(sx+sy)

print(round(3.5)) # 5 is rounded up
print("math module")
import math # module

pi = 3.14 # BTW math. is the way you access the module I think
print(math.ceil(pi))
print(math.floor(pi))
print(max(x,iy,iz)) # max / min is possible

# string slicing
print("string slicing")
# slicing = extracting elements 
#           [start:stop:step]
# start = inclusive , stop = exclusive

string2 = "Suavity"

print(string2[0:3])
print(string2[:6])
print(string2[:5:2])
print(string2[::3])
print(string2[1::2])
print(string2[3::])
print(string2[3:])
print(string2[-1])
print(string2[0:-1:-1]) # generates empty space idk why
print(string2[0::-1]) # same result as string[0] idk why AGAIN
print(string2[::-1]) # reversing a string

website1 = "https://google.com"
website2 = "https://youtube.com"

site = slice(8,-4) # (start, stop, step)
print("Site 1 is "+website1[site])
print("Site 2 is "+website2[site])

# EOF