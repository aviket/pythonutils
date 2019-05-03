import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import requests, time
import json
from datetime import datetime


from weather import Ui_Dialog

class AppWindow(QDialog):
   
       
        def __init__(self):
           super().__init__()
           self.ui = Ui_Dialog()
           self.ui.setupUi(self)
           self.ui.pushButton.clicked.connect(self.on_pushButtonWeather_clicked)
           self.cities = ["Mumbai" , "Pune" , "Nasik"]
           self.ui.comboBox.addItems(self.cities)
           self.show()

        def jsonoup(self):
            api_key = "__api_key__"
            city_name = str(self.ui.comboBox.currentText())
            url1 = "http://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=" + api_key
            r = requests.get(url1)
            time.sleep(5)
            cnt = r.content
            y = json.loads(cnt)
            print(y)
            self.country = y["sys"]["country"]
            self.lon = y["coord"]["lon"]
            self.lat = y["coord"]["lat"]
            self.temperature = y["main"]["temp"]
            self.temp_min = y["main"]["temp_min"]
            self.temp_max = y["main"]["temp_max"]
            self.pressure = y["main"]["pressure"]
            self.humidity = y["main"]["humidity"]
            self.wind_speed = y["wind"]["speed"]
            self.sunrise = str(datetime.fromtimestamp(y["sys"]["sunrise"]))
            self.sunset = str(datetime.fromtimestamp(y["sys"]["sunset"]))
            self.ui.label_country.setText(str(self.country))
            self.ui.label_lat.setText(str(self.lat))
            self.ui.label_lon.setText(str(self.lon))
            self.ui.label_temp.setText(str(self.temperature))
            self.ui.label_tmpmax.setText(str(self.temp_max))
            self.ui.label_tmpmin.setText(str(self.temp_min))
            self.ui.label_pressure.setText(str(self.pressure))
            self.ui.label_humidity.setText(str(self.humidity))
            self.ui.label_windspeed.setText(str(self.wind_speed))
            self.ui.label_sunrise.setText(str(self.sunrise))
            self.ui.label_sunset.setText(str(self.sunset))

            
            



        @QtCore.pyqtSlot()
        def on_pushButtonWeather_clicked(self):
            self.jsonoup()
       
app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())