import random


class PasswordGenerator: # Password generator class
    def __init__(self, length, choice):
        self.length = length
        self.choice = choice

    def generate(self):       
        self.length = int(input("Enter password length: "))
        print("Select password type:")
        print("l - Letters only")
        print("n - Numbers only")
        print("s - Special characters only")
        print("a - All characters")
        self.choice = input("Enter your choice (l/n/s/a): ").lower()
        characters = ""
        match self.choice:
            case 'l':
                characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            case 'n':
                characters = "0123456789"
            case 's':
                characters = "!@#$%^&*()"
            case 'a':
                characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
            case _:
                print("Invalid choice")
                return None
            
        password = "".join(random.choices(characters, k=self.length))
        print(f"Generated password: {password}")

        with open("history/password_history.txt", "a") as f: # Save to history/password_history.txt
                f.write(password + "\n")
                print("Password saved to history/password_history.txt")


    