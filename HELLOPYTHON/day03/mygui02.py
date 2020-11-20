import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *


form_class = uic.loadUiType("mygui02.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.button1Function)

    def button1Function(self) :
        a = self.le.text()
        aa =int(a)
        self.te.setText(  
              a+"x 1 = "+str(aa*1)+"\n"+
            a+"x 2 = "+str(aa*2)+"\n"+
            a+"x 3 = "+str(aa*3)+"\n"+
            a+"x 4 = "+str(aa*4)+"\n"+
            a+"x 5 = "+str(aa*5)+"\n"+
            a+"x 6 = "+str(aa*6)+"\n"+
            a+"x 7 = "+str(aa*7)+"\n"+
            a+"x 8 = "+str(aa*8)+"\n"+
            a+"x 9 = "+str(aa*9)
                        )
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()