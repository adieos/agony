print(ord("e")-96) # prints a unicode character of a number (a = 97, b = 98, etc)

def numbres(num1, num2):
    return num1 - num2

print(numbres(num2=4,num1=5))

# variable scopes
var = "Joko Widodo" # global scope (available both outside and inside the fucntions)
def varibale():
    var = "Om Telolet Om" # local scope (only available inside this function)
    print(var)
def faribale():
    print(var)

varibale() # local variables have higher priority compared to global variables
print(var)
varibale()
faribale()
# variable priority list in Python: LEGB
# L = Local
# E = Enclosed
# G = Global
# B = Built-in

# *args = parameter that will pack all arguments into a tuple
#         used so that a funciton can accept a varying amount of arguments, even none !
#         only one "*" allowed to exist in a single function

def sums (*numbres,): # numbres is a tuple. use numbres = list(numbres) to convert it into a list!
    sum = 0 
    for i in numbres:
        sum += i
    return sum
print(sums(7,4,6,2,6,3,5,1,35)) # THIS IS TOTALLY RANDOM NUMBRES WOW

# **kwargs = parameter that will pack all arguments into a dictionary

def yntkts(**jokowi):
    for i,j in jokowi.items():
        print(j,end=" ")

yntkts(siji="yo", loro="ndak", telu="tau", papat="kok", limo="tanya", enem="saya")
print()
print()
print()
print()

# string formats
sovyet = "labour"
unyon = "The {fantasy} of a {society} their {stronghold} secure!"
print("United forever in {} and {},".format("friendship", sovyet)) # {} are called format field
print("Our {2} {1} will ever {0}!".format("endure","republics","mighty","Stalin"))
print("The Great {country} will {verb} through the {time},".format(verb="live",time="ages",country="Soviet Union"))
print(unyon.format(fantasy="dream",society="people",stronghold="fortress"))

# string formats but numbers
numeral = 65
decimal = 2.62144
print("{:.3f}".format(numeral))
print("{:.3f}".format(decimal))
print("{:,}".format(numeral))
print("{:,}".format(decimal))
# ehhh just google it if you ever need some reference in the future
# :b for binary, :o for octal, :x for hexadecimal, :e/:E for scientific notation

# random numbers
import random
x = random.random() # prints random number between 0 and 1, takes no argument
print(x)
y = random.randint(1,6) # prints random whole integer between the range, both values are inclusive
print(y)
chessPiece = ["Pawn","Knight","Bishop","Rook","Queen","king"]
cp = random.choice(chessPiece) # picks one of the thingy
print(cp)
z = [1,2,3,4,5,6,7,8,9,0]
random.shuffle(z) # shuffles the list, pretty self-explanatory
print(z)

# EOF