statement = (2 - 1 > 3) or (-5 * 2 == -10) or (9 + 5 <= 15) or (7 != 4 + 3)
print(statement)

user_name = input("Введите ваше имя: ")
ARM = int(input("Введите номер АРМ: "))

if user_name == "дмитрий":
    if ARM == 1:
        print("Добро пожаловать!")
    else:
        print("Дмитрий, твое рабочее место находится в другой комнате.")
else:
    if (user_name == "ангелина" and ARM == 2) or \
       (user_name == "василий" and ARM == 3) or \
       (user_name == "екатерина" and ARM == 4):
        print("Добро пожаловать!")
    else:
        print("Логин или пароль неверный, попробуйте еще раз.")

grade = float(input("Введите средний балл студента: "))

if grade >= 4.0:
    print("Грейд: A")
elif grade >= 3.0:
    print("Грейд: B")
elif grade >= 2.0:
    print("Грейд: C")
elif grade >= 1.0:
    print("Грейд: D")
elif grade >= 0.0:
    print("Грейд: F")
else:
    print("Некорректное значение среднего балла.")

grade = float(input("Введите средний балл студента: "))

if grade >= 4.0:
    category = "A"
elif grade >= 3.0:
    category = "B"
elif grade >= 2.0:
    category = "C"
elif grade >= 1.0:
    category = "D"
elif grade >= 0.0:
    category = "F"
else:
    category = "Invalid"

match category:
    case "A":
        print("Грейд: A")
    case "B":
        print("Грейд: B")
    case "C":
        print("Грейд: C")
    case "D":
        print("Грейд: D")
    case "F":
        print("Грейд: F")
    case "Invalid":
        print("Некорректное значение среднего балла.")

def create_spreadsheet(title):
    print("Создание электронной таблицы с именем " + title)

create_spreadsheet("Загрузки")

def create_spreadsheet(title, row_count=1000):
    print("Создание электронной таблицы с названием " + title + " with " + str(row_count) + " lines")

create_spreadsheet("Приложения", 10)

def calc_age(current_year, birth_year):
    age = current_year - birth_year
    return age

my_age = calc_age(2024, 2005)

dads_age = calc_age(2024, 1968)

print(f"Мне {my_age} лет, а моему отцу {dads_age} лет")

def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = target + margin
    return low_limit, high_limit

low_limit, high_limit = get_boundaries(100, 20)

print(f"Нижний предел: {low_limit}, верхний предел: {high_limit}")

def repeat_stuff(stuff, num_repeats=10):
    return stuff * num_repeats

print(repeat_stuff("Row", 3))

lyrics = repeat_stuff("Row", 3) + "Your Boat."

song = repeat_stuff("Row")

print(song)
print(lyrics)
