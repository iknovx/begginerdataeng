import random 

def chiguni():
    print("Welcome to the Chiguni Game!")
    print("You will play against the computer.")
    while True:
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue      
        print(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
                 print("You win!")
        else:
            print("You lose!")
        if input("Do you want to play again? (yes/no): ").lower() != 'yes':
            break
        
chiguni()