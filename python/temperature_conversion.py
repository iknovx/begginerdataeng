class Temperature_Converter: # Simple temperature converter class
    def __init__(self, choice, temp):
        self.choice = choice
        self.temp = temp

    def convert(self):
        print("Select conversion type:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        
        self.choice = int(input("Enter your choice (1/2): "))
        self.temp = float(input("Enter the temperature: "))

        if self.choice == 1:
            result = (self.temp * 9/5) + 32
            print(f"{self.temp}°C is {result}°F")
            text = f"{self.temp}°C is {result}°F"

        elif self.choice == 2:
            result = (self.temp - 32) * 5/9
            print(f"{self.temp}°F is {result}°C")
            text = f"{self.temp}°F is {result}°C"

        else:
            print("Invalid choice")
            return
        # Save to history/temperature_history.txt
        with open("history/temperature_history.txt", "a") as f:
            f.write(text + "\n" + str(self.choice))
        print("Conversion saved to history/temperature_history.txt")
