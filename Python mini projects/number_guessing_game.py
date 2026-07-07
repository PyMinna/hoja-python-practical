import random

def generate_number():
    return random.randint(1, 100)

def get_guess():
    guess = int(input("Enter your guess(1-100): "))
    return guess

def check_guess(secret, guess):
    if guess < secret:
        print("Too Low!")
        return False

    elif guess > secret:
        print("Too High!")
        return False

    else:
        print("Correct!")
        return True
    
def play_game():
    secret_number = generate_number()
    attempts = 0
    max_attempts = 10

    print("=====Number Guessing Game=====")
    print("Guess a number between 1 and 100")
    print("You have only 10 attempts\n")

    while attempts < max_attempts:
        guess = get_guess()
        attempts += 1

        if check_guess(secret_number,guess):
            print("Attempts= ",attempts)
            return
            
        print("Remaining attempts: ",max_attempts - attempts)
        print()

    print("Game Over!")
    print("The correct number was: ",secret_number)

def main():
  
    play_game()
    
main()

    

