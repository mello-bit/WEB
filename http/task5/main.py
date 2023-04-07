import sys
from io import BytesIO

import requests
from PIL import Image
import json


def search_district(coordinates):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": coordinates,
        "format": "json",
        "kind": "district"
    }

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        print("Неверно были определены координаты объекта")
        return None

    json_response = response.json()
    with open("data.json", "w") as file:
        json.dump(json_response, file, indent=3)

    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]

    district = []
    components = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"]

    for item in components:
        if item["kind"] == "district":
            district.append(item["name"])

    return ", ".join(district)


def search_coordinates(address: str):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": address,
        "format": "json"
    }

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        print("Ваш адрес неправильный или содержит ошибки.")

        return None

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


address_to_find = " ".join(sys.argv[1:])

address_ll = ','.join(search_coordinates(address_to_find))

if address_ll is not None:
    print(address_ll)

    district = search_district(address_ll)

    if district is not None:
        print(district)
