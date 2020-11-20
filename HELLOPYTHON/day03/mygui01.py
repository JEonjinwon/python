import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *


form_class = uic.loadUiType("mygui01.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.button1Function)

    def button1Function(self) :
        a = self.lea.text()
        b = self.leb.text()
        aa =int(a)
        bb =int(b)
        c = aa+bb
        cc = str(c)
        self.lec.setText(cc)
 

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()