import random
import time 
from math import sqrt

def calculator():
    while True: 
        print("Simple Calculator")
        print("Select operation: ")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Calculate Square")
        print("6. Calculate Roots")
        choice = int(input("Enter choice (1/2/3/4/5/6): "))
    
        if choice == 7:
           break

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        match choice:
            case 1:
                print(f"{a} + {b} = {a + b}")
            case 2:
                print(f"{a} - {b} = {a - b}")
            case 3: 
                print(f"{a} * {b} = {a * b}")
            case 4:
                if b != 0:
                    print(f"{a} / {b} = {a / b}")
                else:
                    print("Error: Division by zero")
            case 5:
                print(f"The square of {a} is {a ** 2}")
                print(f"The square of {b} is {b ** 2}")
            case 6:
                print(f"The square root of {a} is {sqrt(a)}")
                print(f"The square root of {b} is {sqrt(b)}")
            case _:
                print("Invalid input")

    
def generator():
    length = int(input("Enter the length of the password: "))
    print("Do you need only letters, numbers, or symbols?")
    choice = input("Enter 'l' for letters, 'n' for numbers, 's' for symbols, 'a' for all: ")
    if choice == 'l':
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif choice == 'n':
        characters = "0123456789"
    elif choice == 's':
        characters = "!@#$%^&*()"
    else:
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = "".join(random.choices(characters, k=length))
    print("Generated password is:", password)
    if password:
        with open("password.txt", "a") as f:
            f.write(password + "\n")
            print("Password saved to password.txt")
    


class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    def introduce(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")
        self.city = input("Enter your city: ")
        print(f"Hello, my name is {self.name}, I am {self.age} years old and I live in {self.city}.")



def select_menu():
    while True:
       print("Welcome to the Selector")
       print("1. Generate Password")
       print("2. Simple Calculator")
       print("3. Person Introduction")
       print("4. Exit")
       choice = int(input("Enter your choice: "))
       if choice == 5:
        break
       match choice:
          case 1:
            generator()
          case 2:
            calculator()
          case 3:
            person = Person("", "", "")
            person.introduce()
          case 4:
            print("Exiting...")
            time.sleep(1)
            return
          case _:
            print("Invalid choice, please try again.")
select_menu()

