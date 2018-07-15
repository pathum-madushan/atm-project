# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitoring_person.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ui_Monitoring_person(object):
    def setupUi(self, Ui_Monitoring_person):
        Ui_Monitoring_person.setObjectName("Ui_Monitoring_person")
        Ui_Monitoring_person.resize(676, 506)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Users/Pathum/Desktop/interfaces/10-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Ui_Monitoring_person.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Ui_Monitoring_person)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_cam = QtWidgets.QLabel(self.centralwidget)
        self.lbl_cam.setGeometry(QtCore.QRect(80, 110, 281, 251))
        self.lbl_cam.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_cam.setText("")
        self.lbl_cam.setObjectName("lbl_cam")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 80, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 130, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 210, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txt_time = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_time.setGeometry(QtCore.QRect(460, 130, 131, 20))
        self.txt_time.setObjectName("txt_time")
        self.txt_date = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_date.setGeometry(QtCore.QRect(460, 200, 131, 20))
        self.txt_date.setObjectName("txt_date")
        self.btn_snap = QtWidgets.QPushButton(self.centralwidget)
        self.btn_snap.setGeometry(QtCore.QRect(170, 380, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_snap.setFont(font)
        self.btn_snap.setObjectName("btn_snap")
        self.btn_logout = QtWidgets.QPushButton(self.centralwidget)
        self.btn_logout.setGeometry(QtCore.QRect(490, 410, 75, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_logout.setFont(font)
        self.btn_logout.setObjectName("btn_logout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 40, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        Ui_Monitoring_person.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Ui_Monitoring_person)
        self.statusbar.setObjectName("statusbar")
        Ui_Monitoring_person.setStatusBar(self.statusbar)

        self.retranslateUi(Ui_Monitoring_person)
        QtCore.QMetaObject.connectSlotsByName(Ui_Monitoring_person)

    def retranslateUi(self, Ui_Monitoring_person):
        _translate = QtCore.QCoreApplication.translate
        Ui_Monitoring_person.setWindowTitle(_translate("Ui_Monitoring_person", "Monitoring_person"))
        self.label.setText(_translate("Ui_Monitoring_person", "Live Feed"))
        self.label_2.setText(_translate("Ui_Monitoring_person", "Time:"))
        self.label_3.setText(_translate("Ui_Monitoring_person", "Date:"))
        self.btn_snap.setText(_translate("Ui_Monitoring_person", "Snapshot"))
        self.btn_logout.setText(_translate("Ui_Monitoring_person", "Logout"))
        self.label_4.setText(_translate("Ui_Monitoring_person", "Monitoring person "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui_Monitoring_person = QtWidgets.QMainWindow()
    ui = Ui_Ui_Monitoring_person()
    ui.setupUi(Ui_Monitoring_person)
    Ui_Monitoring_person.show()
    sys.exit(app.exec_())

