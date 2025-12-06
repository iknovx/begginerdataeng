from python.temperature_conversion import Temperature_Converter
from python.password_generator import PasswordGenerator 
from python.currency_convertor import Currency_Converter
from python.calculator import calculator
from python.person import Person
from python.calendar1 import display_calendar 
from python.school_class import SchoolClasses




def select_menu(): # Menu to select different functionalities
    while True:
       print("Welcome to the Selector")
       print("1. Generate Password")
       print("2. Simple Calculator")
       print("3. Person Introduction")
       print("4. Currency Converter")
       print("5. Temperature Converter")
       print("6. Calendar")
       print("7. Exit")
       choice = int(input("Enter your choice: "))
       match choice:
          case 1: # Made with class(OOP)
            password_gen = PasswordGenerator(0, "")
            password = password_gen.generate()
            if password: 
                print(f"Generated Password: {password}")
            break
          case 2: # Made with simple function
            calculator()
            break
          case 3: # Made with class(OOP)
            person = Person("", "", "", "", 0)
            person.introduce()
            break
          case 4: # Made with class(OOP)
            converter = Currency_Converter()
            converter.convert()
            break
          case 5: # Made with class(OOP)
            temperature_converter = Temperature_Converter(0, 0.0)
            temperature_converter.convert()
            break
          case 6: # Made with simple function
            display_calendar()
          case 7:
            school_classes = SchoolClasses("", "", 0)
            school_classes.class_info()
            break
          case _:
            print("Invalid choice, please try again.")
select_menu()

