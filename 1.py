greeting = "Hello, world!"
print(greeting)

length = 8
width = 10

area = length * width
print(f"Площадь комнаты: {area} квадратных метров")

length = 20
area = length * width
print(f"Обновленная площадь комнаты: {area} квадратных метров")

length = 23
width = 13

area = length * width
print(f"Площадь прямоугольника: {area} квадратных метров")

print((6 * 6) - 1 == 8 + 1)
print(13 - 7 != (3 * 2) + 1)
print(3 * (2 - 1) == 4 - 1)
print((6 * 6) - 1 >= 8 + 1)
print(13 - 7 <= (3 * 2) + 1)
print(3 * (2 - 1) > 4 - 1)

bool_variable = 'true'
print(type(bool_variable))
print(bool_variable)

bool_variable_2 = True
print(type(bool_variable_2))
print(bool_variable_2)

user_name = input("Введите ваше имя: ")

dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"

general_message = "Добро пожаловать"

if user_name == "Дмитрий":
    print(dmitriy_check)
else:
    print(general_message)

enter_number = 0

while enter_number < 3:
    password = input("Введите пароль: ")

    if password == "1234":
        print("Пароль верный. Добро пожаловать!")
        break
    else:
        enter_number += 1

        if enter_number < 3:
            print(f"Попробуйте еще раз. У вас осталось {3 - enter_number} попыток.")

if enter_number >= 3:
    print("Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки.")

statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
print(statement_one)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)
print(statement_two)

user_name = input("Введите ваше имя: ")
ARM = int(input("Введите номер АРМ: "))

if user_name == "Дмитрий" and ARM == 1:
    print("Добро пожаловать!")
elif user_name == "Ангелина" and ARM == 2:
    print("Добро пожаловать!")
elif user_name == "Василий" and ARM == 3:
    print("Добро пожаловать!")
elif user_name == "Екатерина" and ARM == 4:
    print("Добро пожаловать!")
elif user_name == "Дмитрий" and ARM != 1:
    print("Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!")
else:
    print("Логин или пароль неверный, попробуйте еще раз.")
