list = [1, 2, 3, 4, 5]
list.append(int(input("Enter a number to add to the list: ")))
print(list)
list.sort(reverse=True)
print(list)

for item in list:
    if item % 2 == 0:
        print(f"{item} is even")
    else:
        print(f"{item} is odd")
sum_of_elements = sum(list)
print(f"Sum of all elements in the list: {sum_of_elements}")
       