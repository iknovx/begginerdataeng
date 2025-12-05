import requests
import json


class Currency_Converter: # Currency converter using API
    def __init__(self):
        self.api_url = "https://api.exchangerate-api.com/v4/latest/USD"

    def convert(self):
        amount = float(input("Enter amount: "))
        from_val = input("From (USD/EUR/GBP/TRY/RUB/BYN/CNY): ").upper()
        to_val = input("To (USD/EUR/GBP/TRY/RUB/BYN/CNY): ").upper()

        response = requests.get(self.api_url)
        data = response.json()
        rates = data['rates']

        if from_val not in rates or to_val not in rates:
            print("Такой валюты нет.")
            return

        # Сonversion calculation
        amount_in_usd = amount / rates[from_val]
        result = amount_in_usd * rates[to_val]

        # Saving data to JSON file
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"{amount} {from_val} = {result} {to_val}")

        # Saving conversion history
        with open("history/conversion_history.txt", "a") as f:
            f.write(f"{amount} {from_val} = {result} {to_val}\n")
        print("Conversion saved to history/conversion_history.txt")

        return result
    

