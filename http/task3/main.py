import sys
from io import BytesIO

import requests
from count_delta import count_delta
from PIL import Image
import json

toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "lang": "ru_RU",
    "results": "1",
    "format": "json",
}

req = requests.get(geocoder_api_server, params=geocoder_params)


if not req:
    print("Sorry. Your request is wrong!!!")
    sys.exit()


json_response = req.json()
# Получаем первый топоним из ответа геокодера.
toponym = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]
# Координаты центра топонима:
toponym_coodrinates = toponym["Point"]["pos"]

toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

delta = count_delta(toponym["boundedBy"]["Envelope"]["lowerCorner"],
                    toponym["boundedBy"]["Envelope"]["upperCorner"])

# ищем аптеку
pharmacy_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "ll": ",".join([toponym_longitude, toponym_lattitude]),
    "lang": "ru_RU",
    "result": "1",
    "format": "json",
    "type": "biz",
    "geocode": "аптека"
}

req_pharmacy = requests.get(geocoder_api_server, params=pharmacy_params)

if not req_pharmacy:
    print("Sorry. Your request is wrong!!! I can't find any pharmacy")
    sys.exit()


json_response = req_pharmacy.json()
with open("data.json", "w") as f:
    json.dump(json_response, f, indent=3)
# Получаем первый топоним из ответа геокодера.
toponym = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]
# Координаты центра топонима:
toponym_coodrinates = toponym["Point"]["pos"]
pharmacy_longitude, pharmacy_lattitude = toponym_coodrinates.split(" ")



map_params = {
    "ll": ",".join([toponym_longitude, toponym_lattitude]),
    "pt": ",".join([pharmacy_longitude, pharmacy_lattitude]),
    "l": "map"
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
# ... и выполняем запрос
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()
# Создадим картинку
# и тут же ее покажем встроенным просмотрщиком операционной системы


