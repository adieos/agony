# looping

n = 3 # how many times the for loop will run

for i in range(n): # i stands for index (starts with 0), n is exclusive
    print(i)

for i in range(25,38): # remember, 25 is inclusive, 30 is exclusive!
    print(i)

for i in range(20,27,2): # PRO TIP: Shift + Enter to run certain block of code
    print(i)

for i in "Sussy":
    print(i+"us")

import time

# for i in range(3,0,-1):
  #  print(i)
   # time.sleep(1) # Sleeps the program for 1 seconds
    
# nested loop
# row = int(input("How many rows? "))
# column = int(input("How many columns? "))
# symbol = str(input("What symbol to use? "))

# non-nested loop variation
#for i in range(row):
   # print(symbol*column)

# print("="*50)
# nested loop variation
# for i in range(row):
    # for j in range(column):
       # print(symbol, end="") # end="" prevents from making a new line 
   # print()

# loop manipulations
# break =  terminates the loop entirely
# continue = skips the current iteration
# pass =  does nothing, acts as a placeholder

# while True:
  #  name = input("Whats nama bpkkau? ")
   # if name != "":
    #    print("yaaa"+name)
     #   break
   # print("jawab atuh!")

president = "JokoWidodo"
for i in president:
    if i == "o" or i == "i":
        continue
    print(i,end="")

print()
for i in range(1,6):
    if i == 4:
        pass
    else:
        print(i)

# list aka array NOTE: chessPiece.append , chessPiece = class? (list), append = attribute
chessPiece = ["pawn","knight","bishop","queen"]
chessPiece.append("king") # adds an element to the end of the list
chessPiece.remove(chessPiece[2]) # removes an element from the list
chessPiece.pop() # removes an element, expected argument is index, default is last or -1
chessPiece.insert(2,"rook") # inserts an element, args: (index,element) NOTE: be careful when using negative num
for i in chessPiece:
    if i == chessPiece[-1]:
        print(i+".")
    else :
        print(i+", ", end="")
chessPiece.clear() # nukes the list

# tuples (uneditable list)
vienna = ("e4","e5","Nc3")
vienna.count("e4") # how many times a certain element exists in the tuple
vienna.index("Nc3") # locate where a certain element is in the tuple
if "d4" in vienna:
    print("WTF thats not vienna")
else:
    print("o k")

# sets (unordered, unindexed, and no-duplicate list)
veggies = {"cucumber","carrot","eggplant","cucumber"} # the last cucumber doesnt actually exist I think
for i in veggies:
    print(i) # will NOT always return the following order: cucumber -> carrot -> eggplant , since they are unindexed

veggies.add("pepper")
veggies.remove("carrot")
veggies.clear() # nukes the set
print("veggies nuked trololololol")
veggies = {"cucumber","carrot","eggplant","cucumber"}
greenvegs = {"lettuce","cabbage","spinach","broccoli","cucumber"}
veggies.update(greenvegs) # conflates two sets. if you try to use .add(), it will raise an error
for i in veggies:
    print(i)

eww = greenvegs.union(veggies) # creates a new set that is a conflation from two sets
print("cherrybbbbbbbb")
for i in greenvegs:
    print(i)

color1 = {"red","green","aqua"}
color2 = {"orange","aqua","magenta"}
print(color1.difference(color2)) # prints elements in color1 that doesnt exist in color2
print(color2.difference(color1)) # prints elements in color2 that doesnt exist in color1
print(color1.intersection(color2)) # prints elements that both color1 and color2 have

# dictionary (key:value paired list)
names = {
    "Magnus":"Carlsen",
    "Shakhriyar":"Mamedyarov",
    "Anatoly":"Karpov",
    "Garry":"Kasparov" }

print(names["Magnus"]) # would return an error if there are no matching key
print(names.get("Viswanathan"))
print(names.get("Anatoly"))
print(names.keys()) # prints only the keys
print(names.values()) # prints only the vlaues
print(names.items()) # prints the whole dict
names.update({"Mikhail":"Tal"}) # can be used to change a value based on a key, but does NOT work vice versa
names.pop("Anatoly") # erases a key-value pair out of existence

for k, v in names.items(): # k = key, v = value
    print("Chess player "+k,v,"is cool")

names.clear() # nukes the dictionary

#indexing
sentence = " Muhyidin bin Wahyudi"
print(sentence[0].islower())

# EOF