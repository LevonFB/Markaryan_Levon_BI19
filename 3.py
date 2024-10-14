product_list = ["торт", 1]

print(product_list)

household_chemicals = [
    ["стиральный порошок", 1],
    ["средство для мытья посуды", 1]
]

print(household_chemicals)

names = ['Ben', 'Holly', 'Ann']
dogs_names = ['Sharik', 'Gab', 'Beethoven']

names_and_dogs_names = zip(names, dogs_names)

list_of_names_and_dogs_names = list(names_and_dogs_names)

print(list_of_names_and_dogs_names)

orders = ['маргаритки', 'васильки']
print("Заказы, полученные сегодня:", orders)

orders.append('тюльпаны')

orders.append('розы')

print("Обновленные заказы, полученные сегодня:", orders)


orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']

new_orders = orders + ['сирень', 'ирис']
print("Обновленный список заказов:", new_orders)


broken_prices = [5, 3, 4, 5, 4]

broken_prices.append(4)

print("Обновленный список цен:", broken_prices)

list1 = list(range(0, 9))

list2 = list(range(0, 7))

print("list1:", list1)
print("list2:", list2)

list1 = list(range(5, 16, 3))

list2 = list(range(0, 40, 5))

print("list1:", list1)
print("list2:", list2)

first_names = ['Анна', 'Борис', 'Александр', 'Денис']

age = []

age.append(42)


anna_boris_alexander_ages = [32, 41, 29]
all_ages = anna_boris_alexander_ages + age

name_and_age = list(zip(first_names, all_ages))

ids = list(range(4))

print("first_names:", first_names)
print("age:", age)
print("all_ages:", all_ages)
print("name_and_age:", name_and_age)
print("ids:", ids)

list1 = list(range(2, 20, 2))
list1_len = len(list1)

print("Длина list1 с шагом 2:", list1_len)

list1 = list(range(2, 20, 3))
list1_len = len(list1)

print("Длина list1 с шагом 3:", list1_len)

shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'сок', 'хлопья']
print("Длина списка покупок:", len(shopping_list))

last_element = shopping_list[-1]

element5 = shopping_list[5]

print("Элемент с индексом 5:", element5)
print("Последний элемент списка:", last_element)

suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']

beginning = suitcase[0:2]
print("Первые два элемента списка:", beginning)

print("Количество элементов в beginning:", len(beginning))

beginning = suitcase[0:4]
print("Первые четыре элемента списка:", beginning)

middle = suitcase[2:4]
print("Средние два элемента списка:", middle)

suitcase = ['рубашка', 'футболка', 'носки', 'очки', 'пижама', 'книги']

start = suitcase[0:3]

print("Первые три элемента списка:", start)

votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie',
         'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']

jake_votes = votes.count('Jake')

print("Количество голосов за Jake:", jake_votes)

addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace',
             '1600 Pennsylvania Ave', '10 Downing St.']

addresses.sort()

print("Отсортированные адреса:", addresses)

games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']

games_sorted = sorted(games)

print("Исходный список игр:", games)
print("Отсортированный список игр:", games_sorted)

# Список inventory
inventory = ["двухспальная кровать", "двухспальная кровать", "изголовье", "двуспальная кровать",
             "двуспальная кровать", "комод", "комод", "стол", "стол", "тумбочка",
             "тумбочка", "королевский кровать", "двуспальная кровать", "две односпальные кровати",
             "две односпальные кровати", "простыни", "простыни", "подушка", "подушка"]

inventory_len = len(inventory)
print("Количество товаров на складе:", inventory_len)

first = inventory[0]
print("Первый элемент инвентаря:", first)

last = inventory[-1]
print("Последний элемент инвентаря:", last)

inventory_2_6 = inventory[2:6]
print("Предметы с индекса 2 до 6 (не включая):", inventory_2_6)

first_3 = inventory[0:3]
print("Первые три предмета инвентаря:", first_3)

twin_beds = inventory.count("две односпальные кровати")
print("Количество односпальных кроватей в инвентаре:", twin_beds)

inventory.sort()
print("Отсортированный инвентарь:", inventory)
