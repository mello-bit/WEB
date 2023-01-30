import requests
import os
import json
import pygame


api_key = "5d666306-8732-43c4-a011-a9cc7afada11"

cities = ["Москва", "Санкт-Петербург", "Рязань", "Ярославль"]
objs = []
num = 0
poses = []

for city in cities:
    req = requests.get(
        f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode={city}&format=json&results=1"
    )

    with open("data.json", "w") as file:
        json.dump(req.json(), file, indent=3)

    obj = req.json()
    objs.append(obj)

for city_cor in objs:
    json_res = city_cor
    # print(json_res)
    pos = json_res["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
    pos = ','.join(pos.split(' '))
    poses.append(pos)

    # num += 1
print(poses)
req = requests.get(
    f"https://static-maps.yandex.ru/1.x/?l=map&pl=c:8822DDC0,w:5,{','.join(poses)}&pt=34.341917,57.629565"
)

with open("final_map.png", "wb") as file:
    file.write(req.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load("final_map.png"), (0, 0))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove("final_map.png")
