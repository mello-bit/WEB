import requests
import os
import sys
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt as Q
import json


api_key = "5d666306-8732-43c4-a011-a9cc7afada11"


class MyWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(os.path.join("api_yandex_map", "task9", "main.ui"), self)
        self.z = 1
        self.lc = None
        self.scheme = "map"
        self.dl = None
        self.sd = None
        self.postal_code = None
        self.is_postal_code = None
        self.show_postal_code = True
        self.btnShow.clicked.connect(self.set_image)
        self.map.clicked.connect(self.set_map)
        self.sat.clicked.connect(self.set_sat)
        self.hybrid.clicked.connect(self.set_hybrid)
        self.thr_off.clicked.connect(self.throw_off)
        self.postal_c.clicked.connect(self.show_or_hide_postal_code)
    
    def show_or_hide_postal_code(self):
        t = self.address.text()
        if self.is_postal_code:
            if self.show_postal_code:
                self.address.setText(
                    f"{t}, {self.postal_code}"
                )
                self.show_postal_code = False
            else:
                self.address.setText(
                    f"{', '.join(t.split(', ')[:-1])}"
                )
                self.show_postal_code = True

    def throw_off(self):
        self.z = 1
        self.dl = 0
        self.sd = 0
        self.set_image(fl=True, hasGeos=True)
        self.address.setText("Address: ")

    def set_map(self):
        self.scheme = "map"
        self.set_image()

    def set_sat(self):
        self.scheme = "sat"
        self.set_image()

    def set_hybrid(self):
        self.scheme = "sat,skl"
        self.set_image()

    def set_image(self, fl=False, hasGeos=False):
        if not fl:
            try:
                self.z = min(11, max(1, int(self.ms.text())))
                self.lc = self.location.text()
            except Exception:
                print("Empty fields/field")
                self.z = 1
        if not hasGeos:
            geo = requests.get(
                f"https://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode={self.lc}&results=1&format=json"
            )
            if not geo:
                print("Error location")
                quit()

            with open("data.json", "w") as file:
                json.dump(geo.json(), file, indent=3)

            geo = geo.json()
            full_address = geo["response"]["GeoObjectCollection"]["featureMember"][0][
                "GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]["formatted"]
            self.address.setText(f"Address: {full_address}")
            # geo = geo.json()
            pos = geo["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
            pos = ','.join(pos.split())
            self.dl, self.sd = map(float, pos.split(','))

            try:
                self.postal_code = geo["response"]["GeoObjectCollection"]["featureMember"][0][
                "GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]
                self.is_postal_code = True
            except Exception:
                self.is_postal_code = False
            
        req = requests.get(
            f"https://static-maps.yandex.ru/1.x/?ll={self.dl},{self.sd}&z={self.z}&l={self.scheme}"
        )

        if not req:
            print("Error in request")
            quit()

        with open("map.png", "wb") as file:
            file.write(req.content)

        pixmap = QPixmap("map.png")
        self.image.setPixmap(pixmap)

    def keyPressEvent(self, event) -> None:
        try:
            if event.key() == Q.Key_PageUp:
                self.z = min(11, max(1, self.z + 1))
                self.set_image(True)
            elif event.key() == Q.Key_PageDown:
                self.z = min(11, max(1, self.z - 1))
                self.set_image(True)
            elif event.key() == Q.Key_Up:
                self.sd += 15
                self.sd = min(45, self.sd)
                self.set_image(True, hasGeos=True)
            elif event.key() == Q.Key_Down:
                self.sd -= 15
                self.sd = max(-45, self.sd)
                self.set_image(True, hasGeos=True)
            elif event.key() == Q.Key_Left:
                self.dl -= 15
                self.dl = max(-45, self.dl)
                self.set_image(True, hasGeos=True)
            elif event.key() == Q.Key_Right:
                self.dl += 15
                self.dl = min(45, self.dl)
                self.set_image(True, hasGeos=True)
        except Exception:
            print("Error in keys. Please check your fields and your request!!!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()

    sys.exit(app.exec_())
