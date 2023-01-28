import json
import requests


api_key = "5d666306-8732-43c4-a011-a9cc7afada11"

response = requests.get(
    f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Исторического музея города Москвы (Красная пл-дь, 1)&format=json"
)

with open("data.json", "w", encoding="utf8") as file:
    json.dump(response.json(), file, indent=3)
    response = response.json()

toponym = response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]

toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
toponym_coodrinates = toponym["Point"]["pos"]
print(f"Адрес: {toponym_address}. Координаты: {toponym_coodrinates}")
