from python.temperature_conversion import Temperature_Converter
from python.password_generator import PasswordGenerator 
from python.currency_convertor import Currency_Converter
from python.calculator import calculator
from python.person import Person



def select_menu(): # Menu to select different functionalities
    while True:
       print("Welcome to the Selector")
       print("1. Generate Password")
       print("2. Simple Calculator")
       print("3. Person Introduction")
       print("4. Currency Converter")
       print("5. Temperature Converter")
       print("6. Exit")
       choice = int(input("Enter your choice: "))
       if choice == 6:
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
            person = Person("", "", "", "", 0)
            person.introduce()
            break
          case 4:
            converter = Currency_Converter()
            converter.convert()
            break
          case 5:
            temperature_converter = Temperature_Converter(0, 0.0)
            temperature_converter.convert()
            break
          case _:
            print("Invalid choice, please try again.")
select_menu()

