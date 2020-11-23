import sys

from PyQt5 import uic
from PyQt5.Qt import QRect, QSize
from PyQt5.QtWidgets import *


from PyQt5.QtGui import*




form_class = uic.loadUiType("myomok02.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.idx=0
        self.setupUi(self)
        self.arr2D = [
                        [1,0,0,0,0, 0,0,0,0,0],
                        [0,2,0,0,0, 0,0,0,0,0],
                        [0,0,1,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0]
                    ]
        
        for i in range(0,10):
            for j in range(0,10):
                qpb=QPushButton("",self)        
                if(self.arr2D[i][j]==1):
                    qpb.setIcon(QIcon("1.png"))
                elif(self.arr2D[i][j]==2):
                    qpb.setIcon(QIcon("2.png"))
                else:
                    qpb.setIcon(QIcon("0.png"))
                qpb.setGeometry(QRect(j*40,i*40,40,40))
                qpb.setIconSize(QSize(40,40))
                
    
   

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()