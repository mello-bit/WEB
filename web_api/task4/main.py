import requests
import json


api_key = "5d666306-8732-43c4-a011-a9cc7afada11"


response = requests.get(
    f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Московского Уголовного Розыска (МУРа) «Петровки, 38»&format=json"
)

json_res = response.json()

toponym = json_res["response"]["GeoObjectCollection"]["featureMember"][0]
postol_code = toponym["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]

print(postol_code)
