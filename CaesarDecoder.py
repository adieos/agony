# wow guys i made a decoder 

alphabet = "abcdefghijklmnopqrstuvwxyz"
password = ""
amogus = True
word = input("Enter your encoded password: ")

while amogus:
    try:
        key = int(input("Enter your key: "))
        break
    except ValueError:
        print("Please enter a valid number!")

for char in word:
    pos = alphabet.find(char)
    newpos = (pos-key) % 26
    newchar = alphabet[newpos]
    password += newchar

print("Your decoded password is "+password)