import sys
import os
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi



import sqlite3
import os.path
import numpy as np
import cv2
import re
import datetime
import util

# import time

class login(QtWidgets.QMainWindow):
    def __init__(self):
        super(login, self).__init__()
        loadUi('login.ui', self)
        self.Btn_login.clicked.connect(self.login)

    def massagebox(self, title, message):
        msgbox = QtWidgets.QMessageBox()
        # msgbox.setIcon(QtGui.QMessageBox.warning)
        msgbox.setWindowTitle(title)
        msgbox.setText(message)
        msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgbox.exec_()

    def clearfield1(self):
        self.txt_uname.setText("")
        self.txt_pwd.setText("")
        self.com_utype.setCurrentIndex(0)

    def login(self):
        
        BASE_DIR = os.path.dirname(os.path.abspath("C:/"))
        db_file = "\sqlite"
        db_path = os.path.join(BASE_DIR, db_file, "ATM.db")
        connection = sqlite3.connect(db_path)

        username = self.txt_uname.text()
        Password = self.txt_pwd.text()
        utype = str(self.com_utype.currentText())
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM user WHERE user_type = ? AND user_name = ? AND password = ?", (utype, username, Password))

        result = cursor.fetchall()
        if (len(result) > 0):
            #util.log("{}","login",'log')
            # for r in result:
            #     ut = r[2]
            # util.log('user logged in successfully')

            cur = connection.cursor()
            user = result[0]
            # print(user)
            # print(user[0])
            cur.execute("UPDATE user SET active_user = (?) WHERE user_id=(?)",[1,int(user[0])])
            connection.commit()
            a = util.getUser()
            u_id = a[0]
            util.setid(u_id)
            
            

            if (utype == "Manager"):
                self.manager = manager()
                self.manager.show()
                self.hide()
            else:
                if (utype == "Monitoring_Person"):
                    self.monitoring_person = monitoring_person()
                    self.monitoring_person.show()
                    self.hide()
                else:
                    if (utype == "Admin"):
                        self.Admin = admin()
                        self.Admin.show()
                        self.hide()

        else:
            self.massagebox(
                'Invalid Login', 'Please check your username and password and try again.')
            self.clearfield1()





class admin(QtWidgets.QMainWindow):
    def __init__(self):
        super(admin, self).__init__()
        loadUi('admin.ui', self)
        self.btn_adduser.clicked.connect(self.Add_user)
        self.btn_view.clicked.connect(self.user)
        self.btn_live.clicked.connect(self.live_feed)
        self.btn_record.clicked.connect(self.record_view)
        self.btn_signout.clicked.connect(self.signout)

    def Add_user(self):
        self.hide()
        self.add = Add_user()
        self.add.show()

    def user(self):
        self.hide()
        self.view = user()
        self.view.show()

    def live_feed(self):
        self.hide()
        self.live = live_feed()
        self.live.show()

    def record_view(self):
        self.hide()
        self.record = record_view()
        self.record.show()

    def signout(self):
        self.hide()
        self.log = login()
        self.log.show()


class Add_user(QtWidgets.QMainWindow):
    def __init__(self):
        super(Add_user, self).__init__()
        loadUi('Adduser.ui', self)
        self.btn_submit.clicked.connect(self.submit_user)
        self.btn_exit.clicked.connect(self.exit_main)
       

    def messagebox(self, title, message):
        msgbox = QtWidgets.QMessageBox()
        # msgbox.setIcon(QtGui.QMessageBox.warning)
        msgbox.setWindowTitle(title)
        msgbox.setText(message)
        msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgbox.exec_()

    def clearfield2(self):
        self.txt_Fname.setText("")
        self.txt_lname.setText("")
        self.txt_uname.setText("")
        self.com_utype.setCurrentIndex(0)
        self.txt_email.setText("")
        self.txt_pwd.setText("")
        self.txt_confpwd.setText("")

    def exit_main(self):
        self.hide()
        self.Admin = admin()
        self.Admin.show()



    def submit_user(self):

        fname = self.txt_Fname.text()
        lname = self.txt_lname.text()
        uname = self.txt_uname.text()
        utype = str(self.com_utype.currentText())
        email = self.txt_email.text()
        pwd = self.txt_pwd.text()
        confpwd = self.txt_confpwd.text()

        addressToVerify = str(email)
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

        error = []


        if fname == "":
            error.append('please fill out first name field')

        if not fname.isalpha():
            error.append(' only characters are allowed 1')

        if lname == "":
                error.append('please fill out last name field')

        elif not lname.isalpha():
            error.append( 'only characters are allowed 2')

        if uname == "":
            error.append( 'please fill out user name field')

        elif not uname.isalpha():
            error.append('only characters are allowed 3')

        if utype == "Select Type":
            error.append( 'please select one of these user type')


        if email == "":
            error.append( 'please fill out email field')

        elif (email != "") and (match == None):
            error.append('Enter valid email address')

        

            
        if pwd == "":
            error.append( 'please fill out password field')

        elif not pwd.isalpha():
            error.append( 'only characters are allowed 6')

       
        if confpwd == "":
            error.append('please re enter your password')

        elif pwd != confpwd:
            error.append( 'password confirm 7')
            
    
        if error==[]:

            BASE_DIR = os.path.dirname(os.path.abspath("C:/"))
            db_file = "\sqlite"
            db_path = os.path.join(BASE_DIR, db_file, "ATM.db")
            connection = sqlite3.connect(db_path)

            with connection:
                cur = connection.cursor()
                cur.execute("INSERT INTO user (fname,lname,user_name,user_type,email,password)"
                            " VALUES ('%s','%s','%s','%s','%s','%s')" % (''.join(fname),
                                                                        ''.join(
                                                                            lname),
                                                                        ''.join(uname), ''.join(
                                                                            utype),
                                                                        ''.join(
                                                                            email),
                                                                        ''.join(pwd))


                            )
                self.messagebox('Success !!', 'successfully submitted')
        
            self.clearfield2()
        else:
            e = str(error)
            # x = a.split()
            # print (error)
            self.messagebox('Error !!!', e)

        
   


class user(QtWidgets.QMainWindow, QtWidgets.QTableWidget):
    def __init__(self):
        super(user, self).__init__()
        loadUi('user.ui', self)
        self.btn_delete.clicked.connect(self.delete_user)
        self.btn_exit.clicked.connect(self.exit_main)
        self.btn_filter.clicked.connect(self.filter_user)
        
    
        BASE_DIR = os.path.dirname(os.path.abspath("C:/"))
        db_file = "\sqlite"
        db_path = os.path.join(BASE_DIR, db_file, "ATM.db")
        connection = sqlite3.connect(db_path)

        cursor = connection.cursor()
        result = cursor.execute ("SELECT user_id, user_name, user_type FROM user")

        self.tableWidget.setRowCount(0)
        for row, form in enumerate(result):
            self.tableWidget.insertRow(row)
            for column, item in enumerate(form):
                self.tableWidget.setItem(
                    row, column, QtWidgets.QTableWidgetItem(str(item)))

            for col in [3]:
                chkBoxItem = QtWidgets.QTableWidgetItem()
                chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                chkBoxItem.setCheckState(QtCore.Qt.Unchecked)       
                self.tableWidget.setItem(row,col,chkBoxItem)

    
        
        # indexes = tableWidget.selectionModel().selectedRows()
        # for index in sorted(indexes):
        #     print('Row %d is selected' % index.row())
        #     tableView = QtWidgets.QTableView()
        #     tableModel = QtWidgets.PaletteTableModel()   
        #     tableView.setModel(tableModel)
        #     x = tableView.selectedIndexes ()
        #     print (x)



    # def checkedItems(self):
    #     for index in range(self.count()):
    #         item = self.item(index)
    #         if item.checkState() == Qt.Checked:
    #             yield index, item
    #             index = listWidget.row(item)
    #             print (index)


   
          
    # selected = tableWidget.selectedItems()
    # print (selected)

    def messagebox(self, title, message):
        msgbox = QtWidgets.QMessageBox()
        # msgbox.setIcon(QtGui.QMessageBox.warning)
        msgbox.setWindowTitle(title)
        msgbox.setText(message)
        msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgbox.exec_()

 
                
    def filter_user(self):

        if self.Admin.isChecked() or self.Manager.isChecked() or self.Monitoring_Person.isChecked():

            if self.Admin.isChecked():
                answer = "Admin"
            elif self.Manager.isChecked():
                answer = "Manager"
            elif self.Monitoring_Person.isChecked():
                answer = "Monitoring_Person"
           
        

            BASE_DIR = os.path.dirname(os.path.abspath("C:/"))
            db_file = "\sqlite"
            db_path = os.path.join(BASE_DIR, db_file, "ATM.db")
            connection = sqlite3.connect(db_path)

            cursor = connection.cursor()
            result = cursor.execute (" SELECT user_id, user_name, user_type FROM user WHERE user_type = '%s'" % (answer))
                

            self.tableWidget.setRowCount(0)
            for row, form in enumerate(result):
                self.tableWidget.insertRow(row)
                for column, item in enumerate(form):
                    self.tableWidget.setItem(
                        row, column, QtWidgets.QTableWidgetItem(str(item)))

                for col in [3]:
                    chkBoxItem = QtWidgets.QTableWidgetItem()
                    chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    chkBoxItem.setCheckState(QtCore.Qt.Unchecked)       
                    self.tableWidget.setItem(row,col,chkBoxItem)

        else:
            self.messagebox('Alert !!!',' Please select one of above radio buttons ')

            

    
    def delete_user(self):
        self.confirm = confirm()
        self.confirm.show()

        # list1 = []
    #     for i in range(34):
    #         list1.append(self.tableWidget.item(self.tableWidget.currentRow(), i).text())
    #         print(list1)

        

    def exit_main(self):
        self.hide()
        self.Admin = admin()
        self.Admin.show()



class confirm(QtWidgets.QDialog):
    def __init__(self):
        super(confirm, self).__init__()
        loadUi('confirm.ui', self)
        # self.btn_ok.clicked.connect(self.conf_ok)
        self.btn_cancel.clicked.connect(self.conf_cancel)

    # def conf_ok(self):
    #     BASE_DIR = os.path.dirname(os.path.abspath("C:/"))
    #     db_file = "\sqlite"
    #     db_path = os.path.join(BASE_DIR, db_file, "ATM.db")
    #     connection = sqlite3.connect(db_path)

    #     cursor = connection.cursor()
    #     cursor.execute("DELETE FROM user WHERE)
    #     connection.commit()


    def conf_cancel(self):
        self.hide()
        self.user = user()
        


class live_feed(QtWidgets.QMainWindow,QtWidgets.QLCDNumber):
    def __init__(self):
        super(live_feed, self).__init__()
        loadUi('cam.ui', self)
        self.btn_start.clicked.connect(self.start_cam)
        self.btn_snap.clicked.connect(self.enter_card)
        self.btn_signout.clicked.connect(self.signout)


        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.showtime)
        self.timer.start(1000)

    def showtime(self):
        self.lcdNumber.setNumDigits(9)
        self.lcdNumber.display(QtCore.QTime.currentTime().toString())
        


        # localtime = time.asctime( time.localtime(time.time()) )

        # print ("Local current time :", localtime)


    def start_cam(self):
        self.head_cascade = cv2.CascadeClassifier('HS.xml')
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(5)


        self.timer1 = QtCore.QTimer()
        self.timer1.timeout.connect(self.showtime1)
        self.timer1.start(1000)

    def showtime1(self):
        self.lcdNumber.setNumDigits(9)
        self.lcdNumber.display(QtCore.QTime.currentTime().toString())
        
        

    def update_frame(self):
        ret, self.image = self.capture.read()
        self.image = cv2.flip(self.image, 1)

        head = self.head_cascade.detectMultiScale(self.image)

        for (x, y, w, h) in head:
            cv2.rectangle(self.image, (x, y), (x+w, y+h), (255, 0, 0), 2)

        self.displayImage(self.image, 1)

    def enter_card(self):
        self.head = self.head_cascade.detectMultiScale(self.image)
        for (self.x, self.y, self.w, self.h) in self.head:
            img_cropped = self.image[self.y:self.y +
                                     self.h, self.x:self.x+self.w]

            now = datetime.datetime.now().strftime('%Y_%B_%d_%A_%Hh_%Mm_%Ss')
            cv2.imwrite('img_snap/snap' + str(now) + '.png', img_cropped)

        BASE_DIR = os.path.dirname(os.path.abspath("C:/"))
        db_file = "\sqlite"
        db_path = os.path.join(BASE_DIR, db_file, "ATM.db")
        connection = sqlite3.connect(db_path)

        now = datetime.datetime.now().strftime('%Y_%B_%d_%A_%Hh_%Mm_%Ss')

        bpath = os.getcwd()
        fpath = 'img_snap'
        img_path = os.path.join(bpath, fpath, 'snap' + str(now) + '.png')
        date_time = now

        with connection:
            cur = connection.cursor()
            cur.execute("INSERT INTO record (date_time,image)"
                        " VALUES ('%s','%s')" % (''.join(date_time),
                                                 ''.join(img_path)))

    def signout(self):
        self.hide()
        self.log = login()
        self.log.show()

    def displayImage(self, img, window=1):
        qformat = QtGui.QImage.Format_Indexed8
        if len(img.shape) == 3:
            if img.shape[2] == 4:
                qformat = QtGui.QImage.Format_RGBA8888
            else:
                qformat = QtGui.QImage.Format_RGB888

        outImage = QtGui.QImage(
            img, img.shape[1], img.shape[0], img.strides[0], qformat)
        outImage = outImage.rgbSwapped()

        if window == 1:
            self.lbl_cam.setPixmap(QtGui.QPixmap.fromImage(outImage))
            self.lbl_cam.setScaledContents(True)


class record_view(QtWidgets.QMainWindow):
    def __init__(self):
        super(record_view, self).__init__()
        loadUi('record.ui', self)
        self.btn_browse.clicked.connect(self.record_view)
        self.btn_signout.clicked.connect(self.signout)

    def signout(self):
        self.hide()
        self.log = login()
        self.log.show()
        

    def record_view(self):
        
        bpath = os.getcwd()
        fpath = 'img_snap'
        f_path = os.path.join(bpath, fpath)

        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "File", f_path)
        
        self.lbl_view.setPixmap(QtGui.QPixmap(filepath, _))
        self.lbl_view.show()

        drive, path_and_file = os.path.splitdrive(filepath)

        path, file = os.path.split(path_and_file)
        self.q_iname.setText(file)
        
        


    def exit_main(self):
        self.hide()
        self.Admin = admin()
        self.Admin.show()


class manager(QtWidgets.QMainWindow):
    def __init__(self):
        super(manager, self).__init__()
        loadUi('manager.ui', self)

        self.btn_live.clicked.connect(self.live_feed)
        self.btn_record.clicked.connect(self.record_view)
        self.btn_signout.clicked.connect(self.signout)

    
    def live_feed(self):
        self.hide()
        self.live = live_feed()
        self.live.show()

    def record_view(self):
        self.hide()
        self.record = record_view()
        self.record.show()

    def signout(self):
        self.hide()
        self.log = login()
        self.log.show()


    
class monitoring_person(QtWidgets.QMainWindow):
    def __init__(self):
        super(monitoring_person, self).__init__()
        loadUi('cam.ui', self)

        self.btn_start.clicked.connect(self.live_feed)
        self.btn_signout.clicked.connect(self.signout)

    def live_feed(self):
        self.hide()
        self.live = live_feed()
        self.live.show()

    
    def signout(self):
        self.hide()
        self.log = login()
        self.log.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    log = login()
    log.show()
    sys.exit(app.exec_())
