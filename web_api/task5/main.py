import requests
import os
import sys
import pygame as pg


api_key = "5d666306-8732-43c4-a011-a9cc7afada11"


response = requests.get(
    f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode=Австралии&format=json"
)

if not response:
    print("Error")
    sys.exit(1)

json_res = response.json()

pos = json_res["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
pos = ','.join(pos.split(' '))

req = requests.get(
    f"http://static-maps.yandex.ru/1.x/?ll={pos}&l=map&z=4"
)

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
