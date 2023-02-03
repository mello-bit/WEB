import requests
import os
import sys
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt as Q


api_key = "5d666306-8732-43c4-a011-a9cc7afada11"



class MyWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(os.path.join("api_yandex_map", "task3", "main.ui"), self)
        self.z = 1
        self.dl = None
        self.sd = None
        self.btnShow.clicked.connect(self.set_image)
        
    def set_image(self, fl=False):
        if not fl:
            try:
                self.z = min(11, max(1, int(self.ms.text())))
                self.dl = float(self.lg.text())
                self.sd = float(self.wd.text())
            except Exception:
                print("Empty fields/field")
                self.z = 1
        
        print(self.dl)
        print(self.sd)
        req = requests.get(
            f"https://static-maps.yandex.ru/1.x/?ll={str(self.dl)},{str(self.sd)}&z={self.z}&l=map"
        )
        
        if not req:
            print("Error in request")
            quit()
        
        with open("map.png", "wb") as file:
            file.write(req.content)
        
        pixmap = QPixmap("map.png")
        self.image.setPixmap(pixmap)
    
    def keyPressEvent(self, event) -> None:
        if event.key() == Q.Key_PageUp:
            self.z = min(11, max(1, self.z + 1))
            self.set_image(True)
        elif event.key() == Q.Key_PageDown:
            self.z = min(11, max(1, self.z - 1))
            self.set_image(True)
        elif event.key() == Q.Key_Up:
            self.sd += 15
            self.sd = min(90, self.sd)
            self.set_image(True)
        elif event.key() == Q.Key_Down:
            self.sd -= 15
            self.sd = max(-90, self.sd)
            self.set_image(True)
        elif event.key() == Q.Key_Left:
            self.dl -= 15
            self.dl = max(-90, self.dl)
            self.set_image(True)
        elif event.key() == Q.Key_Right:
            self.dl += 15
            self.dl = min(90, self.dl)
            self.set_image(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()

    sys.exit(app.exec_())
