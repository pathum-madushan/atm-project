# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manager.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ui_Manager(object):
    def setupUi(self, Ui_Manager):
        Ui_Manager.setObjectName("Ui_Manager")
        Ui_Manager.resize(750, 530)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Users/Pathum/Desktop/interfaces/10-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Ui_Manager.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Ui_Manager)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lbl_cam = QtWidgets.QLabel(self.centralwidget)
        self.lbl_cam.setGeometry(QtCore.QRect(60, 100, 351, 301))
        self.lbl_cam.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_cam.setText("")
        self.lbl_cam.setObjectName("lbl_cam")
        self.lbl_time = QtWidgets.QLabel(self.centralwidget)
        self.lbl_time.setGeometry(QtCore.QRect(440, 140, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_time.setFont(font)
        self.lbl_time.setObjectName("lbl_time")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 240, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txt_time = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_time.setGeometry(QtCore.QRect(520, 140, 141, 20))
        self.txt_time.setObjectName("txt_time")
        self.txt_date = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_date.setGeometry(QtCore.QRect(520, 240, 141, 20))
        self.txt_date.setObjectName("txt_date")
        self.btn_snap = QtWidgets.QPushButton(self.centralwidget)
        self.btn_snap.setGeometry(QtCore.QRect(180, 420, 75, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_snap.setFont(font)
        self.btn_snap.setObjectName("btn_snap")
        self.btn_record = QtWidgets.QPushButton(self.centralwidget)
        self.btn_record.setGeometry(QtCore.QRect(400, 420, 101, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_record.setFont(font)
        self.btn_record.setObjectName("btn_record")
        self.btn_signout = QtWidgets.QPushButton(self.centralwidget)
        self.btn_signout.setGeometry(QtCore.QRect(590, 422, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_signout.setFont(font)
        self.btn_signout.setObjectName("btn_signout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 80, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        Ui_Manager.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Ui_Manager)
        self.statusbar.setObjectName("statusbar")
        Ui_Manager.setStatusBar(self.statusbar)

        self.retranslateUi(Ui_Manager)
        QtCore.QMetaObject.connectSlotsByName(Ui_Manager)

    def retranslateUi(self, Ui_Manager):
        _translate = QtCore.QCoreApplication.translate
        Ui_Manager.setWindowTitle(_translate("Ui_Manager", "Manager"))
        self.label.setText(_translate("Ui_Manager", "Manager"))
        self.lbl_time.setText(_translate("Ui_Manager", "Time:"))
        self.label_2.setText(_translate("Ui_Manager", "Date:"))
        self.btn_snap.setText(_translate("Ui_Manager", "Snapshot"))
        self.btn_record.setText(_translate("Ui_Manager", "Privious Record"))
        self.btn_signout.setText(_translate("Ui_Manager", "Sign out"))
        self.label_3.setText(_translate("Ui_Manager", "Live Feed"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui_Manager = QtWidgets.QMainWindow()
    ui = Ui_Ui_Manager()
    ui.setupUi(Ui_Manager)
    Ui_Manager.show()
    sys.exit(app.exec_())

