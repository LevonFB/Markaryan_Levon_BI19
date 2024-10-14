zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"],
    "fire": ["Aries", "Leo", "Sagittarius"],
    "earth": ["Taurus", "Virgo", "Capricorn"],
    "air": ["Gemini", "Libra", "Aquarius"]
}
zodiac_elements["energy"] = "Not a Zodiac element"
print(zodiac_elements["energy"])

caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

caffeine_level["matcha"] = 30
try:
    print("Уровень кофеина в матче:", caffeine_level["matcha"])
except KeyError:
    print("Неизвестный уровень кофеина")

user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384
}

tc_id = user_ids.get("teraCoder", 100000)
print("Идентификатор teraCoder:", tc_id)

stack_id = user_ids.get("superStackSmash", 100000)
print("Идентификатор superStackSmash:", stack_id)

user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384
}
num_exercises = {
    "functions": 10,
    "syntax": 13,
    "control flow": 15,
    "loops": 22,
    "lists": 19,
    "classes": 18,
    "dictionaries": 18
}

users = user_ids.keys()
classes = num_exercises.keys()

print("Ключи словаря user_ids (users):", users)
print("Ключи словаря num_exercises (classes):", classes)

num_exercises = {
    "functions": 10,
    "syntax": 13,
    "control flow": 15,
    "loops": 22,
    "lists": 19,
    "classes": 18,
    "dictionaries": 18
}

total_exercises = 0

for value in num_exercises.values():
    total_exercises += value

print("Общее количество упражнений:", total_exercises)

tarot = {
    1: "The Magician", 2: "The High Priestess", 3: "The Empress", 4: "The Emperor",
    5: "The Hierophant", 6: "The Lovers", 7: "The Chariot", 8: "Strength",
    9: "The Hermit", 10: "Wheel of Fortune", 11: "Justice", 12: "The Hanged Man",
    13: "Death", 14: "Temperance", 15: "The Devil", 16: "The Tower",
    17: "The Star", 18: "The Moon", 19: "The Sun", 20: "Judgement",
    21: "The World", 22: "The Fool"
}

spread = {}
spread["прошлое"] = tarot.pop(13)
spread["настоящее"] = tarot.pop(22)
spread["будущее"] = tarot.pop(10)

print("Карты Таро (прошлое, настоящее, будущее):", spread)
