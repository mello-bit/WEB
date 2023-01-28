import requests
import json


api_key = "5d666306-8732-43c4-a011-a9cc7afada11"

cities = ["Барнаул", "Мелеуз", "Йошкар-Ола"]

for city in cities:
    response = requests.get(
        f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode={city}&format=json"
    )
    json_res = response.json()

    toponym = json_res["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    area = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][3]

    print(f"Областью города {city} является: {area['name']}")
