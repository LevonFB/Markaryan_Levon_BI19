favour_word = "бум"
print(favour_word)

first_name = "Виталий"
last_name = "Красилов"

new_account = last_name[:5]
print("Имя пользователя:", new_account)

temp_password = last_name[2:6]
print("Временный пароль:", temp_password)

def account_generator(first_name, last_name):
    first_part = first_name[:3]
    last_part = last_name[:3]
    return first_part + last_part

new_account = account_generator("Виталий", "Красилов")

print("Новое имя учетной записи:", new_account)

def password_generator(first_name, last_name):
    first_part = first_name[-3:]
    last_part = last_name[-3:]
    return first_part + last_part

temp_password = password_generator("Виталий", "Красилов")

print("Временный пароль:", temp_password)

company_motto = "Мечты сбываются"

second_to_last = company_motto[-2]
print("Предпоследний символ:", second_to_last)

final_word = company_motto[-4:]
print("Последние 4 символа:", final_word)

first_name = "Доб"

fixed_first_name = "Р" + first_name[1:]

print("Исправленное имя:", fixed_first_name)

password = "theycallme\"crazy\"91"

print("Пароль:", password)

def get_length(input_string):
    count = 0  #
    for char in input_string:
        count += 1
    return count

example_string = "Привет, мир!"
string_length = get_length(example_string)

print("Количество символов в строке:", string_length)

def letter_check(word, letter):
    return letter in word

result = letter_check("Привет", "и")
print("Содержится ли буква в слове?", result)

result = letter_check("Привет", "х")
print("Содержится ли буква в слове?", result)

def contains(big_string, little_string):
    return little_string in big_string

print(contains("watermelon", "melon"))  # Ожидается True
print(contains("watermelon", "berry"))  # Ожидается False

def common_letters(string_one, string_two):
    set_one = set(string_one)
    set_two = set(string_two)
    common = set_one.intersection(set_two)
    return list(common)

print(common_letters("banana", "cream"))  # Ожидается ['a']
print(common_letters("hello", "world"))   # Ожидается ['o', 'l']


def username_generator(first_name, last_name):
    if len(first_name) < 3:
        first_part = first_name
    else:
        first_part = first_name[:3]

    if len(last_name) < 4:
        last_part = last_name
    else:
        last_part = last_name[:4]

    return first_part + last_part


username = username_generator("Abe", "Simpson")
print("Имя пользователя:", username)


def password_generator(username):
    password = ""


    password = username[-1] + username[:-1]

    return password

temp_password = password_generator(username)
print("Временный пароль:", temp_password)
