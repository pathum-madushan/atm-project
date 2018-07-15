# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Admin(object):
    def setupUi(self, Admin):
        Admin.setObjectName("Admin")
        Admin.resize(724, 540)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Users/Pathum/Desktop/interfaces/10-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Admin.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Admin)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_adduser = QtWidgets.QPushButton(self.centralwidget)
        self.btn_adduser.setGeometry(QtCore.QRect(200, 160, 141, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_adduser.setFont(font)
        self.btn_adduser.setObjectName("btn_adduser")
        self.btn_privilage = QtWidgets.QPushButton(self.centralwidget)
        self.btn_privilage.setGeometry(QtCore.QRect(200, 250, 141, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_privilage.setFont(font)
        self.btn_privilage.setObjectName("btn_privilage")
        self.btn_view = QtWidgets.QPushButton(self.centralwidget)
        self.btn_view.setGeometry(QtCore.QRect(200, 340, 141, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_view.setFont(font)
        self.btn_view.setObjectName("btn_view")
        self.btn_signout = QtWidgets.QPushButton(self.centralwidget)
        self.btn_signout.setGeometry(QtCore.QRect(504, 432, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_signout.setFont(font)
        self.btn_signout.setObjectName("btn_signout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 70, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        Admin.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Admin)
        self.statusbar.setObjectName("statusbar")
        Admin.setStatusBar(self.statusbar)

        self.retranslateUi(Admin)
        QtCore.QMetaObject.connectSlotsByName(Admin)

    def retranslateUi(self, Admin):
        _translate = QtCore.QCoreApplication.translate
        Admin.setWindowTitle(_translate("Admin", "Admin"))
        self.btn_adduser.setText(_translate("Admin", "Add new user"))
        self.btn_privilage.setText(_translate("Admin", "Custormize Privilages"))
        self.btn_view.setText(_translate("Admin", "View User"))
        self.btn_signout.setText(_translate("Admin", "Sign out"))
        self.label.setText(_translate("Admin", "Admin"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Admin = QtWidgets.QMainWindow()
    ui = Ui_Admin()
    ui.setupUi(Admin)
    Admin.show()
    sys.exit(app.exec_())

