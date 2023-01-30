import requests
import sys
import json


api_key = "5d666306-8732-43c4-a011-a9cc7afada11"

place = input("Введите название места: ")

req = requests.get(
    f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode={place}&format=json&results=1"
)
if not req:
    print("Error")
    sys.exit(1)

req = req.json()
pos = req["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
pos = pos.split()

new_req = requests.get(
    f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode={','.join(pos)}&format=json&results=1&kind=metro"
)
with open("metro.json", "w") as file:
    json.dump(new_req.json(), file, indent=3)

name = new_req.json()[
    "response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["name"]
print(f"Ближайшая станция метро это {name}")
