price = 100
price = str(price)
if isinstance(price, float):
    print("price is float")
elif isinstance(price, int):
    print("price is int")
else:
    print("price is str")
print(price)