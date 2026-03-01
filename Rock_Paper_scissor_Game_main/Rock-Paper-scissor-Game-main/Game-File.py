import random
choices = {"p" : "Paper", "r" : "Rock", "s" : "Scissors"}
def win(player,computer):
    if ((player == "r" and computer == "s") or
       (player == "s" and computer == "p") or
       (player == "p" and computer == "r")):
       return True
    return False
def game():
    while True:
        ch = input("p for papper and r for Rock and s for siccors and q for quit! ")
        print(f"You choses : {choices[ch]}")
        if ch == "q":
            print("Thanks for playing my game")
            return
        computer = random.choice(["p","r","s"])
        print(f"Computer choses : {choices[computer]}")
        if ch == computer:
            print("Game Tie!")
        elif win(ch,computer):
            print("You Won!")
        else:
            print("Computer Won!")
game()
