import requests
import os
import sys
import pygame as pg
import json


api_key = "5d666306-8732-43c4-a011-a9cc7afada11"
clubs = ["Спартак", "Динамо", "Лужники"]
# clubs = ["Спартак"]


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


def get_clubs_pos(clubs, pos) -> list:
    clubs_pos = []
    for club in clubs:
        res = requests.get(
            f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode={club}&format=json"
        )
        if not res:
            print("Error in `get_club_pos` function!!!")
            sys.exit(1)
        with open(f"{club}.json", "w") as file:
            json.dump(res.json(), file, indent=3)

        res = res.json()
        objs = res["response"]["GeoObjectCollection"]["featureMember"]

        for obj in objs:
            text = obj["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]["formatted"]
            info = obj["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"]
            print(text)
            if info[2]["name"] == "Москва":
                pos = obj["GeoObject"]["Point"]["pos"]
                pos = pos.split()
                clubs_pos.append(f"{pos[0]},{pos[1]},pmntl")
                print(pos)
                break

    return clubs_pos


response = requests.get(
    f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Москва&format=json"
)

if not response:
    print("Error")
    sys.exit(1)

json_res = response.json()

pos = json_res["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
pos = ','.join(pos.split(' '))
clubs_pos = get_clubs_pos(clubs, pos)

req = requests.get(
    f"http://static-maps.yandex.ru/1.x/?ll={pos}&l=map&pt={'~'.join(clubs_pos)}&z=9"
)

show_image()
