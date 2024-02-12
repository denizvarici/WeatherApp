from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap

import sys
from MainWindow import Ui_MainWindow

import getweather
import json


import requests
from io import BytesIO

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnGetInfo.clicked.connect(self.get_daily_weather_info)
        self.ui.cbxCities.currentIndexChanged.connect(self.get_daily_weather_info)

    def get_daily_weather_info(self):
        try:
            #data = getweather.get_daily_weather(self.ui.tbxCity.text())
            data = getweather.get_daily_weather(self.ui.cbxCities.currentText())
            weather_results = data.get("result",[])  
            today_results = weather_results[0]
            self.ui.lblDate.setText(today_results.get("date"))
            self.load_image_from_url(today_results.get("icon"))
            self.ui.lblDay.setText(today_results.get("day"))
            self.ui.lblWeatherState.setText(today_results.get("description"))
            self.ui.lblDegree.setText(today_results.get("degree"))
        except Exception as e:
            self.showError()


    def showError(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setText("Hata! Lütfen şehir ismini kontrol edip tekrar deneyiniz.")
        msg_box.setWindowTitle("Uyarı")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.setDefaultButton(QMessageBox.Ok)

    def load_image_from_url(self, url):
        try:
            # Resmi URL'den indir
            response = requests.get(url)
            response.raise_for_status()  # Hata varsa bir HTTPError fırlatır

            # Resmi QPixmap'e çevir ve QLabel içinde göster
            pixmap = QPixmap()
            pixmap.loadFromData(BytesIO(response.content).read())
            self.ui.lblIcon.setPixmap(pixmap)

        except Exception as e:
            print(f'Hata oluştu: {e}')

    

def app():
    app = QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())


app()