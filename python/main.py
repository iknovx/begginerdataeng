import random
import requests
from math import sqrt
import json



def calculator(): # Simple calculator function
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
        if self.choice == 'l':
            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        elif self.choice == 'n':
            characters = "0123456789"
        elif self.choice == 's':
            characters = "!@#$%^&*()"
        else:
            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        password = "".join(random.choices(characters, k=self.length))
        
        if password:
            with open("password.txt", "a") as f:
                f.write(password + "\n")
                print("Password saved to password.txt")
            return password

    


class Person: # Person class for introduction simple OOP example
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    def introduce(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")
        self.city = input("Enter your city: ")
        print(f"Hello, my name is {self.name}, I am {self.age} years old and I live in {self.city}.")



class Hobby: # Hobby class for describing hobbies
    def __init__(self, hobby_name, years_practiced):
        self.hobby_name = hobby_name
        self.years_practiced = years_practiced
        self.years_practiced = 0
    def describe_hobby(self):
        self.hobby_name = input("Enter your hobby:")
        self.years_practiced = input("Enter years practiced: ")
        if not self.years_practiced.isdigit():
            print("Please enter a valid number for years practiced.")
            return
        print(f"My hobby is {self.hobby_name} and I have been practicing it for {self.years_practiced} years.")


class Currency_Converter:
    def __init__(self):
        self.api_url = "https://api.exchangerate-api.com/v4/latest/USD"

    def convert(self):
        amount = float(input("Введите сумму: "))
        from_val = input("Из валюты (USD/EUR/GBP/TRY/RUB/BYN/CNY): ").upper()
        to_val = input("В валюту (USD/EUR/GBP/TRY/RUB/BYN/CNY): ").upper()

        response = requests.get(self.api_url)
        data = response.json()
        rates = data['rates']

        if from_val not in rates or to_val not in rates:
            print("Такой валюты нет.")
            return

        # Конвертация: сначала → USD, потом → нужную валюту
        amount_in_usd = amount / rates[from_val]
        result = amount_in_usd * rates[to_val]

        # Сохраняем JSON красиво
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"{amount} {from_val} = {result} {to_val}")

        # Сохраняем историю конвертаций
        with open("conversion_history.txt", "a") as f:
            f.write(f"{amount} {from_val} = {result} {to_val}\n")
        print("Conversion saved to conversion_history.txt")

def select_menu(): # Menu to select different functionalities
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
            password_gen = PasswordGenerator(0, "")
            password = password_gen.generate()
            if password:
                print(f"Generated Password: {password}")
            break
          case 2:
            calculator()
            break
          case 3:
            person = Person("", "", "")
            person.introduce()
            hobby = Hobby("", 0)
            hobby.describe_hobby()
            break
          case 4:
            converter = Currency_Converter()
            converter.convert()
            break
          case _:
            print("Invalid choice, please try again.")
select_menu()

