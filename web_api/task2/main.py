import json
import requests


api_key = "5d666306-8732-43c4-a011-a9cc7afada11"

cities = ["Хабаровск", "Уфа", "Нижний Новгород", "Калининград"]

for city in cities:
    response = requests.get(
        f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode={city}&format=json"
    )
    json_res = response.json()

    toponym = json_res["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]

    areas = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"]
    for area in areas:
        if "федеральный округ" in area["name"]:
            print(f"Федеральный округ города {city}: {area['name']}")
