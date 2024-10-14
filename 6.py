poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()

print("Название стихотворения:", poem_title_fixed)
print("Автор стихотворения:", poem_author)

line_one = "The sky has given over"

line_one_words = line_one.split()

print("Список слов:", line_one_words)

authors = "Audre Lorde, Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

author_names = authors.split(", ")

print("Список имен авторов:", author_names)

author_last_names = [name.split()[-1] for name in author_names]

print("Список фамилий авторов:", author_last_names)

spring_storm_text = """The sky has given over
its bitterness.

Out of the dark change
all day long
rain falls and falls
as if it would never end.
Still the snow keeps
its hold on the ground.
But water, water
from a thousand runnels!
It collects swiftly,
dappled with black
cuts a way for itself
through green ice in the gutters.
Drop after drop it falls
from the withered grass-stems
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.splitlines()

print("Список строк стихотворения:", spring_storm_lines)

sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
sensors["storage"] = 22  # Добавляем датчик для "кладовой"

print("Обновленный словарь датчиков:", sensors)

num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

print("Словарь с количеством камер:", num_cameras)

translations = {
    "mountain": "orod",
    "bread": "bass",
    "friend": "mellon",
    "horse": "roch"
}

print("Словарь переводов:", translations)

animals_in_zoo = {}
animals_in_zoo["зебры"] = 8
animals_in_zoo["обезьяны"] = 12
animals_in_zoo["динозавры"] = 0

print("Животные в зоопарке:", animals_in_zoo)

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids["theLooper"] = 138475
user_ids["stringQueen"] = 85739

print("Обновленный словарь user_ids:", user_ids)

oscar_winners = {
    "Best Picture": "La La Land",
    "Best Actor": "Casey Affleck",
    "Best Actress": "Emma Stone",
    "Animated Feature": "Zootopia"
}

oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"

print("Обновленный словарь oscar_winners:", oscar_winners)

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {drink: mg for drink, mg in zipped_drinks}

print("Словарь напитков и их содержания кофеина:", drinks_to_caffeine)

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {song: count for song, count in zip(songs, playcounts)}

print("Словарь plays:", plays)

plays["Purple Haze"] = 1
plays["Respect"] += 5

library = {
    "The Best Songs": plays,
    "Sunday Feelings": {}
}

print("Словарь library:", library)

zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"],
    "fire": ["Aries", "Leo", "Sagittarius"],
    "earth": ["Taurus", "Virgo", "Capricorn"],
    "air": ["Gemini", "Libra", "Aquarius"]
}

earth_signs = zodiac_elements["earth"]
print("Знаки зодиака стихии земля:", earth_signs)

fire_signs = zodiac_elements["fire"]
print("Знаки зодиака стихии огонь:", fire_signs)

