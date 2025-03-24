import random 

def guessing_game():
    """
    A simple number guessing game where the user tries to guess a random number between 1 and 100.
    """
    number = random.randint(1, 5)  # Generate a random number
    guesses_left = 3  # Set the number of guesses allowed 
    
    print("Welcome to the Guessing Game!")
    print("Think of a number between 1 and 100.") 
    
    while guesses_left > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        guesses_left -= 1 
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! YOU WIN! {number} in {10 - guesses_left} tries!")
            break
    
    if guesses_left == 0:
        print(f"OBOI TRY AGAIN The number was {number}.")

if __name__ == "_main_":
   guessing_game()