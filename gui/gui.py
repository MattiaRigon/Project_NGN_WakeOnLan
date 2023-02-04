# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

elenco_docker= ["docker1","docker2","docker3","docker4","docker5"]
docker_selected = ""

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 30, 671, 41))
        self.textEdit.setObjectName("textEdit")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(60, 90, 671, 351))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 669, 349))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.radioButton = []
        i=0
        for item in elenco_docker :
            self.radioButton.append(QtWidgets.QRadioButton(self.scrollAreaWidgetContents))
            self.radioButton[i].setGeometry(QtCore.QRect(30, 40 + i*30, 112, 23))
            self.radioButton[i].setObjectName("radioButton")
            self.radioButton[i].clicked.connect(self.check)

            i=i+1

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.turnonButton = QtWidgets.QPushButton(self.centralwidget)
        self.turnonButton.setGeometry(QtCore.QRect(160, 490, 201, 51))
        self.turnonButton.setObjectName("turnonButton")
        self.turnonButton.clicked.connect(self.turnonCallback)
        self.turnofButton = QtWidgets.QPushButton(self.centralwidget)
        self.turnofButton.setGeometry(QtCore.QRect(440, 490, 201, 51))
        self.turnofButton.setObjectName("turnofButton")
        self.turnofButton.clicked.connect(self.turnofCallback)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">LIST OF DOCKERS</span></p></body></html>"))
        i=0
        for item in elenco_docker :
            self.radioButton[i].setText(_translate("MainWindow", item))
            i=i+1
        self.turnonButton.setText(_translate("MainWindow", "Turn ON"))
        self.turnofButton.setText(_translate("MainWindow", "Turn OFF"))

  
    # method called by radio button
    def check(self):

        global docker_selected

        for radio_button in self.radioButton : 
            # checking if it is checked
            if radio_button.isChecked():
                
                # changing docker_selected
                docker_selected = radio_button.text()
    
    # method called by Turn On button
    def turnonCallback(self):

        global docker_selected

        print("Richiesta TURN ON docker : " + docker_selected)


    # method called by Turn Off button
    def turnofCallback(self):

        global docker_selected

        print("Richiesta TURN OFF docker : " + docker_selected)
    
    
        
  