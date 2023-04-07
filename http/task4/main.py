import sys
from io import BytesIO

import requests
from PIL import Image
import json


def length_of_the_way(cors1, cors2):
    deltaX = abs(float(cors1[0]) - float(cors2[0]))
    deltaY = abs(float(cors1[1]) - float(cors2[1]))

    return (deltaX ** 2 + deltaY ** 2) ** 0.5


def search_coordinates(address: str):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": address,
        "format": "json"
    }

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        # обработка ошибочной ситуации
        pass

    # Преобразуем ответ в json-объект
    json_response = response.json()
    # Получаем первый топоним из ответа геокодера.
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    # Координаты центра топонима:
    toponym_coordinates = toponym["Point"]["pos"]
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coordinates.split(" ")
    return toponym_longitude, toponym_lattitude


api_key = "245ecbd7-5831-42f5-99a3-24305300d58b"
search_api_server = f"https://search-maps.yandex.ru/v1/"
map_api_server = "http://static-maps.yandex.ru/1.x/"
list_of_coordinates = []

address_to_find = " ".join(sys.argv[1:])

address_ll = ','.join(search_coordinates(address_to_find))
print(address_ll)

search_params = {
    "text": "аптека",
    "lang": "ru_RU",
    "type": "biz",
    "apikey": api_key,
    "ll": address_ll,
}

response = requests.get(search_api_server, params=search_params)

if not response:
    # ...
    print("JJJJJJJJJ")
    pass

json_response = response.json()
with open("data.json", "w") as f:
    json.dump(json_response, f, indent=3)

# проходимся циклом до конца списка(либо до 10) и подставляем индекс за место числа в квадратных скобках
for index in range(len(json_response["features"])):
    organization = json_response["features"][index]

    org_coordinates = organization["geometry"]["coordinates"]
    try:
        hours = organization["properties"]["CompanyMetaData"]["Hours"]
        if hours["Availabilities"]:
            try:
                if hours["Availabilities"][0]["Everyday"]:
                    list_of_coordinates.append(
                        "{0},{1},pm2dgm".format(
                            org_coordinates[0], org_coordinates[1])
                    )
            except KeyError:
                list_of_coordinates.append(
                    "{0},{1},pm2blm".format(
                        org_coordinates[0], org_coordinates[1])
                )
    except KeyError:
        list_of_coordinates.append(
            "{0},{1},pm2grm".format(org_coordinates[0], org_coordinates[1])
        )

delta = "0.05"

map_params = {
    "ll": address_ll,
    "spn": ",".join([delta, delta]),
    "l": "map",
    # добавим точку, чтобы указать найденную аптеку
    "pt": '~'.join(list_of_coordinates)
}


response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()
