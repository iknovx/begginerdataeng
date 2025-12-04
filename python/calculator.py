from math import sqrt


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

        if choice > 6 or choice < 1:
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
        print()  # Blank line for better readability

