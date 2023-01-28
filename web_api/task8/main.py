import requests
import sys
import json


api_key = "5d666306-8732-43c4-a011-a9cc7afada11"

cities = input(
    "Введите список городов через запятую(без пробела): ").split(',')
positions = []

for city in cities:
    city = city.strip()
    req = requests.get(
        f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode={city}&format=json&results=1"
    )

    if not req:
        print("Не правильно был указан список городов!")
        sys.exit(1)

    with open("data.json", "w") as file:
        json.dump(req.json(), file, indent=3)

    req = req.json()

    kind = req["response"]["GeoObjectCollection"]["featureMember"][0]
    kind = kind["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["kind"]

    if kind != "province" and kind != "locality":
        continue

    try:
        pos = req["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
        pos = pos.split()
        positions.append([pos, city])
    except IndexError:
        print(f"Город {city} не был найден.")


positions = sorted(positions, key=lambda p: float(p[0][1]))
# print(positions)
try:
    ct, wd = positions[0][-1], positions[0][0][-1]
    print(f"Южнее всех находится город {ct} с широтой {wd}")
except IndexError:
    print("Список пуст. В нем нет городов")
