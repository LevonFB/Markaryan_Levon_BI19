import csv
import json
from datetime import datetime

# Исходные данные о сотрудниках
employees = [
    {"ФИО": "Иванов Иван Иванович", "Должность": "Менеджер", "Дата найма": "22.10.2013", "Оклад": 250000},
    {"ФИО": "Сорокина Екатерина Матвеевна", "Должность": "Аналитик", "Дата найма": "12.03.2020", "Оклад": 75000},
    {"ФИО": "Струков Иван Сергеевич", "Должность": "Старший программист", "Дата найма": "23.04.2012", "Оклад": 150000},
    {"ФИО": "Корнеева Анна Игоревна", "Должность": "Ведущий программист", "Дата найма": "22.02.2015", "Оклад": 120000},
    {"ФИО": "Старчиков Сергей Анатольевич", "Должность": "Младший программист", "Дата найма": "12.11.2021", "Оклад": 50000},
    {"ФИО": "Бутенко Артем Андреевич", "Должность": "Архитектор", "Дата найма": "12.02.2010", "Оклад": 200000},
    {"ФИО": "Савченко Алина Сергеевна", "Должность": "Старший аналитик", "Дата найма": "13.04.2016", "Оклад": 100000}
]

# Создаем CSV файл с данными о сотрудниках
with open("employees.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["ФИО", "Должность", "Дата найма", "Оклад"])
    writer.writeheader()
    writer.writerows(employees)

# Функция для расчета премии ко дню программиста
def calculate_programmer_bonus(employees):
    for emp in employees:
        if "программист" in emp["Должность"].lower():
            emp["Премия"] = emp["Оклад"] * 0.03

# Функция для расчета премии к 8 марта и 23 февраля
def calculate_holiday_bonus(employees):
    for emp in employees:
        emp["Премия"] = emp.get("Премия", 0) + 2000

# Функция для индексации зарплат сотрудников
def index_salary(employees):
    current_year = datetime.now().year
    for emp in employees:
        years_of_service = current_year - datetime.strptime(emp["Дата найма"], "%d.%m.%Y").year
        if years_of_service > 10:
            emp["Оклад"] *= 1.07
        else:
            emp["Оклад"] *= 1.05

# Функция для составления графика отпусков
def create_vacation_schedule(employees):
    vacation_schedule = []
    current_date = datetime.now()
    for emp in employees:
        hire_date = datetime.strptime(emp["Дата найма"], "%d.%m.%Y")
        months_of_service = (current_date.year - hire_date.year) * 12 + (current_date.month - hire_date.month)
        if months_of_service > 6:
            vacation_schedule.append(emp["ФИО"])
    return vacation_schedule

# Расчет премий и индексации зарплат
calculate_programmer_bonus(employees)
calculate_holiday_bonus(employees)
index_salary(employees)

# Составляем график отпусков сотрудников
vacation_schedule = create_vacation_schedule(employees)
print("График отпусков:", vacation_schedule)

# Записываем обновленные данные в CSV и JSON
with open("updated_employees.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["ФИО", "Должность", "Дата найма", "Оклад", "Премия"])
    writer.writeheader()
    writer.writerows(employees)

with open("employees.json", mode="w") as file:
    json.dump(employees, file, ensure_ascii=False, indent=4)
