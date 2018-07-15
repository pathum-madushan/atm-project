import PyQt5
import sqlite3
import getpass
import os
import json
import datetime


# class system():

def getUser():
    BASE_DIR = os.path.dirname(os.path.abspath("C:/"))
    db_file = "\sqlite"
    db_path = os.path.join(BASE_DIR, db_file, "ATM.db")
    connection = sqlite3.connect(db_path)
    
    
    cursor = connection.cursor()
    cursor.execute ("SELECT user_id,user_name,user_type FROM user WHERE active_user = %s"%(1)) 
    
    user = cursor.fetchall()
    if (len(user) > 0):
            # for r in user:
            #     ut = r[2]
            #     print (ut )
        result = user[0]
        print(result)
        return result


def setid(u_id):
    BASE_DIR = os.path.dirname(os.path.abspath("C:/"))
    db_file = "\sqlite"
    db_path = os.path.join(BASE_DIR, db_file, "ATM.db")
    connection = sqlite3.connect(db_path)
    
    
    cursor = connection.cursor()
    cursor.execute ("UPDATE user SET active_user = (?) WHERE user_id=(?)",[0,u_id])
    connection.commit()

        
        
        # SELECT and get active user
        # SELECT user_id FROM user WHERE
        # print('get user')

    # def setUser():
    #     print('set user')


def log(data,action,etype):

    print(getUser())
    user_id = getUser()['id']

    datetime.datetime.now()

    BASE_DIR = os.path.dirname(os.path.abspath("C:/"))
    db_file = "\sqlite"
    db_path = os.path.join(BASE_DIR, db_file, "ATM.db")
    connection = sqlite3.connect(db_path)

    with connection:
        cur = connection.cursor()
        cur.execute("INSERT INTO log (data,user_id,timestamp,action,e_type)"
                    " VALUES ('%s','%s','%s','%s','%s')" % (''.join(data),
                                                                ''.join(
                                                                    user_id),
                                                                ''.join(
                                                                    action),
                                                                    ''.join(
                                                                    timestamp),
                                                                ''.join(
                                                                    etype)))
