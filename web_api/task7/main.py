import requests
import os
import sys
import pygame as pg
import json


api_key = "5d666306-8732-43c4-a011-a9cc7afada11"
main_obj = "Санкт-Петербург"
start = "Петергоф"
end = "Дворцовая площадь, 2, Санкт-Петербург"


def get_way_cors(center_pos):
    start_pos, end_pos = "", ""

    req = requests.get(
        f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode={start}&format=json&ll={center_pos}"
    )
    req_end = requests.get(
        f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode={end}&format=json&results=100&ll={center_pos}"
    )

    with open("way.json", "w") as file:
        json.dump(req.json(), file, indent=3)

    with open("end.json", "w") as file:
        json.dump(req_end.json(), file, indent=3)

    req = req.json()
    objs = req["response"]["GeoObjectCollection"]["featureMember"]

    req_end = req_end.json()
    objs2 = req_end["response"]["GeoObjectCollection"]["featureMember"]

    for obj in objs:
        text = obj["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]["formatted"]
        info = obj["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"]
        if text.split(', ')[2] == start:
            pos = obj["GeoObject"]["Point"]["pos"]
            print(text)
            print(pos)
            start_pos = ','.join(pos.split())
            print(1)
            break

    for obj2 in objs2:
        text = obj2["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]["formatted"]
        info = obj2["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"]
        pos = obj2["GeoObject"]["Point"]["pos"]
        print(text)
        print(pos)
        end_pos = ','.join(pos.split())

    return start_pos, end_pos


def show_image():
    with open("map.png", "wb") as file:
        file.write(req.content)

    pg.init()

    screen = pg.display.set_mode((600, 450))

    screen.blit(pg.image.load("map.png"), (0, 0))
    pg.display.flip()

    while pg.event.wait().type != pg.QUIT:
        pass
    pg.quit()

    os.remove("map.png")


response = requests.get(
    f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode={main_obj}&format=json"
)

if not response:
    print("Error")
    sys.exit(1)

json_res = response.json()

pos = json_res["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
pos = ','.join(pos.split(' '))
start_pos, end_pos = get_way_cors(pos)
print(start_pos, end_pos)
req = requests.get(
    f"http://static-maps.yandex.ru/1.x/?ll={pos}&l=map&z=8&pl={start_pos},{end_pos}"
)

show_image()
