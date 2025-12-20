import random 

def guessGame():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and {}.".format(max_number))
    level = input("Choose a difficulty, easy, medium or hard: ").lower()
    attempts = 0
    if level == 'easy':
        attempts = 10
        max_number = 20
    elif level == 'medium':
        attempts = 7
        max_number = 50
    elif level == 'hard':
        attempts = 5
        max_number = 100
    else:
        print("Invalid difficulty level. Please choose easy, medium, or hard.")
        return
    
    secret_number = random.randint(1, max_number)
    print(f"You have {attempts} attempts to guess the number between 1 and {max_number}.")
    while attempts > 0:
        guess = int(input("Make a guess: "))
        if guess < 1 or guess > max_number:
            print(f"Please guess a number between 1 and {max_number}.")
            continue
        if guess == secret_number:
            print(f"Congratulations! You've guessed the number {secret_number} correctly!")
            return
        elif guess < secret_number:
            print("Too low.")
        else:
            print("Too high.")
        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts remaining.")
        else:
            print(f"Sorry, you've run out of attempts. The number was {secret_number}.")
        if guess < 1 or guess > max_number:
            print(f"Please guess a number between 1 and {max_number}.")

guessGame()