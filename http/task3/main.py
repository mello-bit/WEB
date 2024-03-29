import sys
from io import BytesIO

import requests
from PIL import Image
import json


def get_data_of_company(json_response):
    organization = json_response["features"][0]

    org_name = organization["properties"]["CompanyMetaData"]["name"]
    org_address = organization["properties"]["CompanyMetaData"]["address"]
    hours = organization["properties"]["CompanyMetaData"]["Hours"]["text"]

    return {
        "address": org_address,
        "name": org_name,
        "hours": hours
    }


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

address_to_find = " ".join(sys.argv[1:])

address_ll = ','.join(search_coordinates(address_to_find))
print(address_ll)

search_params = {
    "text": "аптека",
    "lang": "ru_RU",
    "type": "biz",
    "apikey": api_key,
    "ll": address_ll
}

response = requests.get(search_api_server, params=search_params)

if not response:
    # ...
    print("JJJJJJJJJ")
    pass

json_response = response.json()
with open("data.json", "w") as f:
    json.dump(json_response, f, indent=3)
organization = json_response["features"][0]

org_name = organization["properties"]["CompanyMetaData"]["name"]
org_address = organization["properties"]["CompanyMetaData"]["address"]
org_coordinates = organization["geometry"]["coordinates"]
org_point = "{0},{1}".format(org_coordinates[0], org_coordinates[1])
# delta = "0.005"
lengthOfTheWay = length_of_the_way(address_ll.split(','), org_point.split(','))
delta = str(lengthOfTheWay)

companyMetaData = get_data_of_company(json_response)
companyMetaData["length of the way"] = f"{lengthOfTheWay * 111.111} км"

print(companyMetaData)


map_params = {
    "ll": address_ll,
    "spn": ",".join([delta, delta]),
    "l": "map",
    # добавим точку, чтобы указать найденную аптеку
    "pt": "{0},pm2dgl".format(org_point) + "~" + "{0}".format(address_ll)
}


response = requests.get(map_api_server, params=map_params)

# with open("map.png", "wb") as map_file:
#     map_file.write(response.content)
Image.open(BytesIO(
    response.content)).show()

# print(org_name)
# print(org_address)
