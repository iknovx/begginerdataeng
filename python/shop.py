class Shop: # Made with class(OOP)
    def __init__(self, name, price, quantity, products):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.choice = input("Enter 1 to view products, 2 to buy a product: ").lower()
        products = [
            {"name": "Apple", "price": 0.5, "quantity": 100},
            {"name": "Banana", "price": 0.3, "quantity": 150},
            {"name": "Orange", "price": 0.7, "quantity": 120}
        ]
        self.products = products

    def product_info(self):
        print("Available Products:")
        for product in self.products:
            info = f"Product: {product['name']}, Price: ${product['price']}, Quantity: {product['quantity']}"
            print(info)
            print("Do u want to buy a product? (yes/no)")
            choice = input().lower()
            if choice == 'yes':
                name = product['name']
                quantity = int(input("Enter the quantity you want to buy: "))
                self.buy_product(name, quantity)
            else:
                print("Okay, continue shopping.")

    def buy_product(self, name, quantity):
        for product in self.products:
            if product['name'].lower() == name.lower():
                if product['quantity'] >= quantity:
                    total_price = product['price'] * quantity
                    product['quantity'] -= quantity
                    print(f"Purchased {quantity} {name}(s) for ${total_price:.2f}")
                else:
                    print(f"Sorry, only {product['quantity']} {name}(s) available.")
                return
        print(f"Product '{name}' not found.")
    
    def shop_run(self):
        if self.choice == '1':
            self.product_info()
        elif self.choice == '2':
            name = input("Enter the product name you want to buy: ")
            quantity = int(input("Enter the quantity you want to buy: "))
            self.buy_product(name, quantity)
        else:
            print("Invalid choice.")
                
            
shop = Shop("", 0.0, 0, [])
shop.shop_run()
