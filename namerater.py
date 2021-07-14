alphabet = " abcdefghijklmnopqrstuvwxyz"
score = 0
name = input("What's your name? ")
name = name.lower()

for i in name:
    if alphabet.find(i) == -1:
        pass
    else:
        amogus = alphabet.find(i)
        score += amogus

if score == 100:
    print("WOW you reached a perfect score!")
elif score == 0:
    print("you so nob youknow")
else:
    score = score % 100
    score = str(score)
    print("Your name is rated "+score)