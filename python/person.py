class Person: # Person class for introduction simple OOP example
    def __init__(self, name, age, city, hobby, years_practiced):
        self.name = name
        self.age = age
        self.city = city
        self.hobby = hobby
        self.years_practiced = years_practiced
    def introduce(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")
        self.city = input("Enter your city: ")
        self.hobby = input("Enter your hobby: ")
        self.years_practiced = input("Enter years practiced: ")
        if not self.years_practiced.isdigit():
            print("Please enter a valid number for years practiced.")
            return
        
        print(f"Hello, my name is {self.name}, I am {self.age} years old and I live in {self.city}. My hobby is {self.hobby} and I have been practicing it for {self.years_practiced} years.")
       
        with open("history/user_history.txt", "a") as f: # Save into history/user_history.txt
            f.write(f"Name: {self.name}, Age: {self.age}, City: {self.city}, Hobby: {self.hobby}, Years Practiced: {self.years_practiced}\n")
            print("Introduction saved to history/user_history.txt")

