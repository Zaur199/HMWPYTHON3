# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.

from itertools import chain, combinations

hike = {'Спальник': 5.0,
        'Палатка': 10.0,
        'Топор': 2.5,
        'Еда': 7.0,
        'Вода': 5.0,
        'Бадминтон': 1.5,
        'Радио': 3.0
    
} 

capacity = int(input('Грузоподъёмность рюкзака: '))
backpack = 0
pack = []

for thing, weight in hike.items():
    if backpack + weight <= capacity:
        backpack += weight
        pack.append(thing)
pack.append(backpack)
print(pack)