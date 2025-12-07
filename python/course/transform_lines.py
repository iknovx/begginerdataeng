price = 100
price = str(price)
if isinstance(price, float):
    print("price is float")
elif isinstance(price, int):
    print("price is int")
else:
    print("price is str")
print(price)

list = [1, 2, 3, 4, 5]
list.append("Hello world")
print(list)
print(list)

print(str(5) + '10')

int_value = 50
float_value = 20.5
sum_value = float_value + int_value
print(sum_value)

boolean_value = True
int_val = 10
sum_bool_int = int_val + boolean_value
print(sum_bool_int)

int_value2 = 23
float_value2 = 12.7
print(int_value2.__add__(float_value2)) # not implemented
print(float_value2.__add__(int_value2)) # implemented = 35.7