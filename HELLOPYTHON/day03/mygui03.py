import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *


form_class = uic.loadUiType("mygui03.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb0.clicked.connect(self.button0Function)
        self.pb1.clicked.connect(self.button1Function)
        self.pb2.clicked.connect(self.button2Function)
        self.pb3.clicked.connect(self.button3Function)
        self.pb4.clicked.connect(self.button4Function)
        self.pb5.clicked.connect(self.button5Function)
        self.pb6.clicked.connect(self.button6Function)
        self.pb7.clicked.connect(self.button7Function)
        self.pb8.clicked.connect(self.button8Function)
        self.pb9.clicked.connect(self.button9Function)
        self.pbc.clicked.connect(self.buttoncFunction)

    def button0Function(self) :
        a = self.pb0.text()
        aa = self.le1.text()
        aaa =aa+a
        self.le1.setText(aaa)
    def button1Function(self) :
        a = self.pb1.text()
        aa = self.le1.text()
        aaa =aa+a
        self.le1.setText(aaa)
    def button2Function(self) :
        a = self.pb2.text()
        aa = self.le1.text()
        aaa =aa+a
        self.le1.setText(aaa)
    def button3Function(self) :
        a = self.pb3.text()
        aa = self.le1.text()
        aaa =aa+a
        self.le1.setText(aaa)
    def button4Function(self) :
        a = self.pb4.text()
        aa = self.le1.text()
        aaa =aa+a
        self.le1.setText(aaa)
    def button5Function(self) :
        a = self.pb5.text()
        aa = self.le1.text()
        aaa =aa+a
        self.le1.setText(aaa)
    def button6Function(self) :
        a = self.pb6.text()
        aa = self.le1.text()
        aaa =aa+a
        self.le1.setText(aaa)
    def button7Function(self) :
        a = self.pb7.text()
        aa = self.le1.text()
        aaa =aa+a
        self.le1.setText(aaa)
    def button8Function(self) :
        a = self.pb8.text()
        aa = self.le1.text()
        aaa =aa+a
        self.le1.setText(aaa)
    def button9Function(self) :
        a = self.pb9.text()
        aa = self.le1.text()
        aaa =aa+a
        self.le1.setText(aaa)
    def buttoncFunction(self) :
        k = self.le1.text()
        QMessageBox.about(self,"전화창 ","전화중 : "+k)
       

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()