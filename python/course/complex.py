from math import sqrt, pow


complex_a = 10j + 5
complex_b = 12 + 3j

complex_sum = complex_a + complex_b
complex_product = complex_a * complex_b
complex_division = complex_a / complex_b
complex_subtraction = complex_a - complex_b
# complex_sqrt = sqrt(complex_a) error should be real number, doesnt work with complex
complex_pow = pow(complex_a, 2)
print("Sum:", complex_sum)
print("Product:", complex_product)
print("Division:", complex_division)
print("Subtraction:", complex_subtraction)
# print("Square Root:", complex_sqrt)
print("Power:", complex_pow)

