import sys
import os
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

# from PyQt5.QtWidgets import QApplication, QLCDNumber
# from PyQt5.QtCore import QTimer , QTime



# from PyQt5.QtWidgets import QApplication, QLCDNumber
# from PyQt5.QtCore import QTimer , QTime


class clock(QtWidgets.QMainWindow,QtWidgets.QLCDNumber):
    def __init__(self):
        super(clock, self).__init__()
        loadUi('cam.ui', self)
        self.btn_start.clicked.connect(self.start_cam)
        self.btn_snap.clicked.connect(self.enter_card)
        self.btn_signout.clicked.connect(self.signout)
        

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.showTime()

    def showtime(self):
        time  = QTime.currentTime()
        text = time.toString('hh:mm')

        if(time.second() % 2) == 0:
            text = text[:2] + '' + text [3:]

        self.display(text)

        # app = QApplication (sys.argv) 
        # live_feed = clock()
        # live_feed.show()
        # app.exec()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    clock = clock()
    clock.show()
    sys.exit(app.exec_())
