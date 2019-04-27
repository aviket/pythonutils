#!/usr/bin/env python
#-*- coding:utf-8 -*-
import csv
import requests
import time 

from PyQt5 import QtCore, QtGui, QtWidgets


from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon

import filedlg

class MyWindow(QtWidgets.QWidget):
    def __init__(self, fileName, parent=None):
        super(MyWindow, self).__init__(parent)
        self.fileName = fileName

        self.model = QtGui.QStandardItemModel(self)

        self.tableView = QtWidgets.QTableView(self)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)

       

        self.pushButtonLoad = QtWidgets.QPushButton(self)
        self.pushButtonLoad.setText("Load Csv File!")
        self.pushButtonLoad.clicked.connect(self.on_pushButtonLoad_clicked)


        self.pushButtonMaps = QtWidgets.QPushButton(self)
        self.pushButtonMaps.setText("Download Maps")
        self.pushButtonMaps.clicked.connect(self.on_pushButtonMaps_clicked)

       
        self.layoutVertical = QtWidgets.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.tableView)
        self.layoutVertical.addWidget(self.pushButtonLoad)
        self.layoutVertical.addWidget(self.pushButtonMaps)
       
        
        

    def openFileDialog(self, fileType):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;" + fileType + " Files (*." +  fileType + ")", options=options)
        if fileName:
           return fileName
        else:
           return None    
    

    

    
    def saveFileDialog(self, fileType):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;" + fileType + " Files (*." +  fileType + ")", options=options)
        if fileName:
           return fileName
        else:
           return None




    def modarr(self,orgarr , pref, suf):
        newarr = []
        api_key  = "_your_map_key_"
        
        for itm in orgarr:
            newarr.append(pref + itm[1] + "," + itm[2] + "&zoom=10&size=400x400&key=" + api_key +   suf)
        return newarr

    def namearr(self, orgarr):
        retarr = []
        for nm in orgarr:
            retarr.append(nm[0])
        return retarr

    def savemaps(self, urlarr, namearr):
        cnt = 0
        folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        folder = folder.replace("/" , "//") + "//"
        for uurl in urlarr:
            
            r = requests.get(uurl)
            time.sleep(5)
            
            f = open(folder + namearr[cnt] + '.png', 'wb') 
            f.write(r.content)
            time.sleep(5)
            cnt = cnt + 1
            


  
    
    
    
    def convertCsv(self):
        
       lst = []
      
       for rowNumber in range(self.model.rowCount()):
          
           fields = [
               self.model.data(
                   self.model.index(rowNumber, columnNumber),
                   QtCore.Qt.DisplayRole
               )
               for columnNumber in range(self.model.columnCount())
           ]
           lst.append(fields)
       return lst
       
    
    def geturllst(self, rawlst):
        for rawitm in rawlst:
            print(rawitm)

   
    
    

    def loadCsv(self, fileName):
        cnt = 0
        #file1 = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        #print(file1)
        #self.modarr(['a','b' , 's'] , 'zz' , 'jj')
        with open(fileName, "r", encoding="utf8") as fileInput:
            for row in csv.reader(fileInput):    
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)
                cnt += 1
       
       

    
    def xstr(s):
       if s is None:
           return ''
       return str(s)  
                 

                

    



    @QtCore.pyqtSlot()
    def on_pushButtonLoad_clicked(self):
        csvfile = self.openFileDialog("csv")
        if csvfile:
            self.loadCsv(csvfile)
        else:
            QMessageBox.warning(self, 'PyQt5 message' , "No CSV file name chosen")

    @QtCore.pyqtSlot()
    def on_pushButtonMaps_clicked(self):
        url1 = "https://maps.googleapis.com/maps/api/staticmap?center="
        urla = self.modarr(self.convertCsv(), url1 , "&sensor=false")
        nmarr = self.namearr(self.convertCsv())
        self.savemaps( urla , nmarr)

   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('MyWindow')
    main = MyWindow("C:\\Users\\avinash\\Downloads\\sample.csv")
    main.show()
    sys.exit(app.exec_())