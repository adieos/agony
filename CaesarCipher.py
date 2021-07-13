alphabet = "abcdefghijklmnopqrstuvwxyz"
password = ""
amogus = True
word = input(str("Enter your password: "))

while amogus:
    try:
        key = int(input("Enter your key: "))
        break
    except ValueError:
        print("Please enter a valid number!")

for char in word:
    pos = alphabet.find(char)
    newpos = (pos+key) % 26
    newchar = alphabet[newpos]
    password += newchar

print("Your new password is "+password)