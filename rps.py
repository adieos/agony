import random
amogus = True # AAAAAAAAAAAAAAAAAAAAA

while amogus:
    impasta = True # HHHHHHHHHHHHHHHHH
    options =  ["rock", "paper", "scissors"]
    computer = random.choice(options)
    while impasta:
        player = input("rock, paper, or scissors? ").lower()
        if player in options:
            impasta = False
        else:
            print("Invalid option!")
    print("Computer: {computer}\nYou: {player}".format(computer=computer,player=player))
    
    if computer == player:
        print("It's a tie!")
    elif (computer == "rock" and player == "scissors") or (computer == "paper" and player == "rock") or (computer == "scissors" and player =="paper"):
        print("You lost!")
    else:
        print("You won!")
    
    while amogus:
        play_again = input("Play again? (y/n): ").lower()
        if play_again == "y":
            break
        elif play_again == "n":
            amogus = False
        else:
            print("Invalid option!")

print("Game ended. Goodbye!")