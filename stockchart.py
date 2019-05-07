import quandl
import numpy as np
import matplotlib.pyplot as plt
import requests
import time 
import json
import math

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from dateutil import parser
from PyQt5.QtCore import QDate


from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMessageBox, QCalendarWidget
from PyQt5.QtGui import QIcon
from stocks import Ui_Dialog

class MyWindow(QtWidgets.QWidget):
  
   def __init__(self):
      super().__init__()
      self.ui = Ui_Dialog()
      self.ui.setupUi(self)
      self.mindatecal = self.ui.dateEdit
      self.maxdatecal = self.ui.dateEdit_2
      self.pushbutton = self.ui.pushButton
      self.slider1 = self.ui.horizontalSlider
      self.labelslider = self.ui.label_3
      api_key = "NJzHnB_ydiT7FL3nFpMx"
      uurl = "https://www.quandl.com/api/v3/datasets/NSE/NIFTY_50.json?api_key=" + api_key
      r = requests.get(uurl)
      jsondat = r.content
      jsonf = json.loads(jsondat)
      print(jsonf["dataset"]["column_names"])
      dat1 = jsonf["dataset"]["data"]
      self.ticks =  [row[0] for row in dat1]
      self.open = [row[1] for row in dat1]
      self.high = [row[2] for row in dat1]
      self.low =  [row[3] for row in dat1]
      self.close = [row[4] for row in dat1]
      self.n_groups = len(self.ticks)
      maxdates = self.ticks[0]
     
      maxdatearr = maxdates.split("-")
      mindates = self.ticks[len(self.ticks) - 1]
      mindatearr = mindates.split("-")
      self.ui.dateEdit.setMaximumDate (QDate(int(maxdatearr[0]) , int(maxdatearr[1]) , int (maxdatearr[2])))
      self.ui.dateEdit.setMinimumDate (QDate(int(mindatearr[0]) , int(mindatearr[1]) ,int(mindatearr[2])))
      self.pushbutton.clicked.connect(self.onMindateChanged)
      self.ui.dateEdit.setDate(QDate(int(mindatearr[0]) , int(mindatearr[1]) , int (mindatearr[2])))
      self.ui.dateEdit_2.setDate(QDate(int(maxdatearr[0]) , int(maxdatearr[1]) , int (maxdatearr[2])))
      self.ui.dateEdit_2.setMaximumDate (QDate(int(maxdatearr[0]) , int(maxdatearr[1]) , int (maxdatearr[2])))
      self.ui.dateEdit_2.setMinimumDate (QDate(int(mindatearr[0]) , int(mindatearr[1]) ,int(mindatearr[2])))
      self.slider1.valueChanged.connect(self.onsliderchanged) 
     
      self.show()
     
      if self.validate():
         self.slider1.setMaximum(100)
         self.slider1.setTickInterval(5)
         self.slider1.setSingleStep(1)
         self.slider1.setSliderPosition(25)
         self.slider1.setTickPosition(25)
         

      
   def modsamples(self, lst ):
      noofbars = self.slider1.value()
      interval = math.ceil(len(lst) / noofbars)
      return lst[::interval]
   


      

      
   def validate(self):
      self.mindate = self.mindatecal.date()
      self.maxdate = self.maxdatecal.date()
      mindatenew = QDate.toPyDate(self.mindate)
      maxdatenew = QDate.toPyDate(self.maxdate)

      self.mdate1 = datetime.strptime(str(mindatenew), "%Y-%m-%d").date()
      self.rdate1 = datetime.strptime(str(maxdatenew), "%Y-%m-%d").date()
      self.delta =  (self.rdate1 - self.mdate1).days

      if self.delta < 0:
          QMessageBox.about(self, "Alert" , "Start Date Should be smaller than End Date")
          return False
      else:
       
         

          return True




   def modsamples1(self):
      startdate = self.ui.dateEdit.date()
      enddate = self.ui.dateEdit_2.date()
      print(startdate)
      print(enddate)
      print(self.ticks[5])
          

   
   def plt(self):
        
      
      # create plot
      fig, ax = plt.subplots()
      index = np.arange(len(self.ticksnew))
      bar_width = 0.175

      opacity = 0.8


      if self.ui.radioButton.isChecked():
         rects1 = plt.bar(index, self.opennew, bar_width,
                         alpha=opacity,
                         color='b',
                         label='Open')
          
         rects2 = plt.bar(index + bar_width, self.closenew, bar_width,
                         alpha=opacity,
                         color='g',
                         label='Close')
      else:
         rects1 = plt.bar(index, self.highnew, bar_width,
                        alpha=opacity,
                        color='b',
                        label='High')
             
         rects2 = plt.bar(index + bar_width, self.lownew, bar_width,
                        alpha=opacity,
                        color='g',
                        label='Low')

      
      
      
      plt.xlabel('Dates')
      plt.ylabel('Index')
      plt.title('Nifty Historical Data')
      plt.xticks(index + bar_width, tuple(self.ticksnew), rotation='vertical')
      plt.legend()
       
      plt.tight_layout()
      plt.show()

   @QtCore.pyqtSlot()
   def onMindateChanged(self):
      if self.validate():
        

         self.ticks1 = []
         self.open1 = []
         self.high1 = []
         self.low1 = []
         self.close1 = []
         for i in range(len(self.ticks)):
            dtarr = self.ticks[i].split("-")
            dtn = QDate(int(dtarr[0]) , int(dtarr[1]) , int (dtarr[2]))
            dtn1 = QDate.toPyDate(dtn)
            if self.mdate1 <= dtn1 and self.rdate1 >= dtn1:
               self.ticks1.append(dtn1)
               self.open1.append(self.open[i])
               self.close1.append(self.close[i])
               self.low1.append(self.low[i])
               self.high1.append(self.high[i])
         self.ticks1 = self.ticks1[::-1]
         self.open1 = self.open1[::-1]
         self.close1 = self.close1[::-1]
         self.low1 = self.low1[::-1]
         self.high1 = self.high1[::-1]

         self.ticksnew = self.modsamples(self.ticks1)
         self.opennew = self.modsamples(self.open1)
         self.closenew = self.modsamples(self.close1)
         self.highnew = self.modsamples(self.high1)
         self.lownew = self.modsamples(self.low1)
         self.plt()


   @QtCore.pyqtSlot()
   def onsliderchanged(self):
       self.labelslider.setText(str(self.slider1.value()))
       self.modsamples1()




if __name__ == "__main__":
   import sys
   app = QtWidgets.QApplication(sys.argv)
   app.setApplicationName('MyWindow')
   main = MyWindow()
   main.show()
   sys.exit(app.exec_())
   



