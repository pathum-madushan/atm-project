self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.showtime)
        self.timer.start(1000)

    def showtime(self):
        self.lcdNumber.setNumDigits(9)
        self.lcdNumber.display(QtCore.QTime.currentTime().toString())
        