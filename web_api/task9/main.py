import requests
import os
import sys
import pygame as pg
import json
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt as Q


api_key = "5d666306-8732-43c4-a011-a9cc7afada11"

cities = ["Санкт-Петербург", "Москва", "Нью-Йорк", "Калифорния", "Токио"]
# cities = ["Санкт-Петербург"]


class MyWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(os.path.join("web_api", "task9", "main.ui"), self)
        self.num = 0
        self.objs = self.get_cities_cors(cities)
        self.make_image()
        self.num = 0
        self.pix = QPixmap(f"map{self.num}.png")
        self.image.setPixmap(self.pix)
        
        self.R.clicked.connect(self.onClickR)
        self.L.clicked.connect(self.onClickL)
    
    def keyPressEvent(self, event) -> None:
        if event.key() == Q.Key_A:
            self.onClickL()
        elif event.key() == Q.Key_D:
            self.onClickR()
    
    def onClickR(self):
        self.num = (self.num + 1) % len(self.objs)
        self.pix = QPixmap(f"map{self.num}.png")
        self.image.setPixmap(self.pix)
    
    def onClickL(self):
        self.num = (self.num - 1) % len(self.objs)
        self.pix = QPixmap(f"map{self.num}.png")
        self.image.setPixmap(self.pix)

    def get_cities_cors(self, cities):
        objs = []
        for city in cities:

            req = requests.get(
                f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode={city}&format=json&results=1"
            )

            with open("data.json", "w") as file:
                json.dump(req.json(), file, indent=3)

            obj = req.json()
            objs.append(obj)

        return objs

    def make_image(self):
        for city_cor in self.objs:
            json_res = city_cor
            # print(json_res)
            pos = json_res["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
            pos = ','.join(pos.split(' '))
            req = requests.get(
                f"http://static-maps.yandex.ru/1.x/?ll={pos}&l=map&z=8&"
            )
            
            with open(f"map{self.num}.png", "wb") as file:
                file.write(req.content)

            
            self.num += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()

    sys.exit(app.exec_())
