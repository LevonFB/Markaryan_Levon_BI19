order = ['паста', 'пицца', 'салат капрезе']

order.append('салат цезарь')
order.append('кофе')

order.append('красное сухое вино')

print("Итоговый заказ:", order)

order = ['паста', 'пицца', 'салат капрезе', 'салат цезарь', 'кофе', 'красное сухое вино']

order.insert(0, 'закуска из овощей')

print("Обновленный заказ:", order)

order = ['закуска из овощей', 'паста', 'пицца', 'салат капрезе', 'салат цезарь', 'кофе', 'красное сухое вино']

order.remove('салат капрезе')

print("Обновленный заказ:", order)

order = ['закуска из овощей', 'паста', 'пицца', 'салат цезарь', 'кофе', 'красное сухое вино']

order.remove('красное сухое вино')

print("Обновленный заказ:", order)

numbers = list(range(8))
print("Исходный список:", numbers)

del numbers[3:5]

print("Обновленный список:", numbers)

x = [15, 11, 13, 12, 14, 10]

x.reverse()
print("Список в обратном порядке (метод reverse):", x)

x = [15, 11, 13, 12, 14, 10]

reversed_x = x[::-1]
print("Список в обратном порядке (срез):", reversed_x)

board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']
sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

for game in board_games:
    print(game)

for sport in sport_games:
    print(sport)

promise = "I will not chew gum in class"

for i in range(5):
    print(promise)

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
    students_period_B.append(student)

    print(student)

print("Список студентов в period_B после объединения:", students_period_B)

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for breed in dog_breeds_available_for_adoption:
    print(breed)

    if breed == dog_breed_I_want:
        print("У них есть собака, которую я хочу!")

        break

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location_sales in sales_data:
    for scoops in location_sales:
        scoops_sold += scoops

print("Общее количество проданных сортов мороженого:", scoops_sold)


single_digits = list(range(10))

squares = []

for digit in single_digits:
    print(digit)
    squares.append(digit ** 2)

print("Список квадратов:", squares)

cubes = [digit ** 3 for digit in single_digits]

print("Список кубов:", cubes)
