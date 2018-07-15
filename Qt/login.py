# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import os.path

from manager import Ui_Ui_Manager
from monitoring_person import Ui_Ui_Monitoring_person
from admin import Ui_Admin
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    
    def massagebox(self,title,message):
        msgbox = QtWidgets.QMessageBox()
        # msgbox.setIcon(QtWidgets.QMessageBox.warning)
        msgbox.setWindowTitle(title)
        msgbox.setText(message)
        msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgbox.exec_() 
    
            
    def openwindow(self):

        BASE_DIR = os.path.dirname(os.path.abspath("C:/"))
        db_file = "\sqlite"
        db_path = os.path.join(BASE_DIR,db_file,"ATM.db")
        connection = sqlite3.connect(db_path)
        # connection.execute("CREATE TABLE USERS(USERNAME TEXT NOT NULL,PASSWORD TEXT)")

        # connection.execute("INSERT INTO USERS VALUES(?,?)",('100','111'))


        # connection.commit()
        
        username = self.txt_uid.text()
        Password = self.txt_pwd.text()
        utype = self.txt_utype.text()

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user WHERE user_type = ? AND user_name = ? AND password = ?",(utype,username,Password))


        result = cursor.fetchall();   

        for r in result:
            ut = r[2]

        if (ut == "Manager"):
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Ui_Manager()
            self.ui.setupUi(self.window) 
            self.window.show()
        else:
            if (ut == "Monitoring_person"):
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_Ui_Monitoring_person()
                self.ui.setupUi(self.window) 
                self.messagebox('valid','valid')
                self.window.show()
            else:
                if (ut == "Admin"):
                    self.window = QtWidgets.QMainWindow()
                    self.ui = Ui_Admin()
                    self.ui.setupUi(self.window) 
                    self.window.show()
                else:
                    print("user not found ")



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Users/Pathum/Desktop/interfaces/10-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_login.setGeometry(QtCore.QRect(260, 330, 221, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Btn_login.setFont(font)
        self.Btn_login.setObjectName("Btn_login")

        self.Btn_login.clicked.connect(self.openwindow)

        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(120, 390, 75, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_close.setFont(font)
        self.btn_close.setObjectName("btn_close")
        self.lbl_uid = QtWidgets.QLabel(self.centralwidget)
        self.lbl_uid.setGeometry(QtCore.QRect(250, 120, 51, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_uid.setFont(font)
        self.lbl_uid.setObjectName("lbl_uid")
        self.lbl_utype = QtWidgets.QLabel(self.centralwidget)
        self.lbl_utype.setGeometry(QtCore.QRect(250, 40, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_utype.setFont(font)
        self.lbl_utype.setObjectName("lbl_utype")
        self.lbl_pwd = QtWidgets.QLabel(self.centralwidget)
        self.lbl_pwd.setGeometry(QtCore.QRect(250, 210, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_pwd.setFont(font)
        self.lbl_pwd.setObjectName("lbl_pwd")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 180, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txt_utype = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_utype.setGeometry(QtCore.QRect(320, 80, 141, 31))
        self.txt_utype.setObjectName("txt_utype")
        self.txt_uid = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_uid.setGeometry(QtCore.QRect(320, 170, 141, 31))
        self.txt_uid.setObjectName("txt_uid")
        self.txt_pwd = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_pwd.setGeometry(QtCore.QRect(320, 250, 141, 31))
        self.txt_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_pwd.setObjectName("txt_pwd")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.Btn_login.setText(_translate("MainWindow", "Login"))
        self.btn_close.setText(_translate("MainWindow", "Close"))
        self.lbl_uid.setText(_translate("MainWindow", "User ID"))
        self.lbl_utype.setText(_translate("MainWindow", "User Type"))
        self.lbl_pwd.setText(_translate("MainWindow", "Password"))
        self.label_4.setText(_translate("MainWindow", "User Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

