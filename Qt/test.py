import sys
import unittest
import os
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
from PyQt5.uic import loadUi

import util
import json

class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_active_logged_user(self):
        self.assertEqual( util.getUser(), None)    

if __name__ == '__main__':
    unittest.main()