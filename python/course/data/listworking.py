people = [
    {'name': 'Dima', 'age': 25},
    {'name': 'John', 'age': 30},
    {'name': 'Alice', 'age': 22},
    {'name': 'Bob', 'age': 28}
]

# сортировка по имени
people.sort(key=lambda x: x['name'])
print(people)

name_input = input("Enter a name: ").capitalize()
age_input = int(input("Enter an age: "))

# поиск человека по имени
person_found = False

for person in people:
    if person['name'] == name_input:
        person['age'] = age_input   # обновляем возраст
        person_found = True
        print(f"Updated {name_input}'s age to {age_input}")
        break

# если имени не было — добавляем нового человека
if not person_found:
    people.append({'name': name_input, 'age': age_input})
    print(f"Added {name_input} with age {age_input}")

# финальная сортировка
people.sort(key=lambda x: x['name'])
print(people)