import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_player_choice():
    while True:
        player = input("Enter Rock, Paper, Scissors: ").lower()

        if player in ["rock", "paper", "scissors"]:
            return player
        else:
            print("invalid choice! Please enter rock,paper,or scissors")


def check_winner(player,computer):
    if player == computer:
        return "it's a Draw!"
    
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win!"
    
    else:
        return "Computer wins!"
    

def play_game():
    player = get_player_choice()
    computer = get_computer_choice()

    print("\nYou chose:", player.capitalize())
    print("computer chose:", computer.capitalize())

    result = check_winner(player,computer)
    print(result)


def main():
    print("=====Rock Paper Scissors Game=====")
    
    while True:
        play_game()
        
        again = input("\nDo you want to play again? (yes/no): ").lower()

        if again != "yes":
            print("Thanks for playing!")
            break

        

main()
