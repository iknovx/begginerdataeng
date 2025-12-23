def logging():
    data = []
    print("Welcome to logging module")
    username = input("Enter your user ID: ")
    print(f"User ID: {username}")
    password = input("Enter your password: ")
    print("Password entered successfully")
    data.append({"username": username, "password": password})
    
    print("Loggin with ur login and password: " )
    print(data)
    for entry in data:
        while True:
            choice = input("Do you want to re-enter your credentials for verification? (yes/no): ").strip().lower()
            if choice in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        if choice == 'yes':
           entry_username = input("Re-enter your username for verification: ")
           entry_password = input("Re-enter your password for verification: ")
           if entry["username"] == entry_username and entry["password"] == entry_password:
               print("Login successful")
           else:
               print("Login failed")
        elif choice == 'no':
            print("Verification skipped")
        else:
            print("Invalid choice. Skipping verification.")
    return data

logging()
    