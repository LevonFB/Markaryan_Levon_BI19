Nail_style = ["Шеллак", "Френч", "Обычный лак", "Гель-лак", "Акрил"]
Price = [2000, 1500, 1000, 3000, 3500]
Week = [4, 5, 4, 8, 6]

# среднее значение посещений салона
average_visits = sum(Week) / len(Week)

# общее количество посещений салона
total_visits = sum(Week)

# выручка салона
total_revenue = sum([Price[i] * Week[i] for i in range(len(Nail_style))])

# выручка по видам маникюра
revenue_by_style = {Nail_style[i]: Price[i] * Week[i] for i in range(len(Nail_style))}

# средняя выручка в день по видам маникюра
average_daily_revenue_by_style = {style: revenue / 7 for style, revenue in revenue_by_style.items()}

print(f"Среднее значение посещений салона: {average_visits}")
print(f"Общее количество посещений салона: {total_visits}")
print(f"Выручка салона: {total_revenue}")
print("Выручка по видам маникюра:")
for style, revenue in revenue_by_style.items():
    print(f"  {style}: {revenue}")
print("Средняя выручка в день по видам маникюра:")
for style, avg_daily_revenue in average_daily_revenue_by_style.items():
    print(f"  {style}: {avg_daily_revenue:.2f}")
