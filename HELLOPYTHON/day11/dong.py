import random
import sys

from PyQt5 import uic, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic.Compiler.qtproxies import QtGui
from openpyxl.drawing.geometry import PresetGeometry2D


form_class = uic.loadUiType("dong.ui")[0]
class Pengsu:
    def __init__(self):#__init__은 constructor 역할  (생성자)  new 하면 생긴다 
        self.i=2 
        self.j=2 
    def __str__(self):
        return "i:"+str(self.i)+"j:"+str(self.j)+""


class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.scrn2D = [
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0]
                                  
                    ]
        self.pang2D = [
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0]
                                  
            
             ]
        self.dong2D = [
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0]
                                  
            
             ]
        self.lbl2D =[]
        self.pangsu = Pengsu()
        self.setupUi(self)
        self.pm0 = QPixmap("image/white.png")
        self.pm1 = QPixmap("image/men.png")
        self.pm2 = QPixmap("image/tex.jpg")


        
        for i in range(5):
            line = []
            for j in range(5): 
                lbl = QLabel(self)
                lbl.setGeometry(80*j,80*i,80,80)
                lbl.resize(80, 80)
                lbl.setScaledContents(True)
                line.append(lbl)
            self.lbl2D.append(line)  
    
        self.setPang2D()
        self.setDong2D()
        self.setScrn2D()
        self.myrender()   
             
    def btn_click(self):
        pass
    
    
    def keyPressEvent(self,e):
        
        key = e.key()
        orign_i = self.pangsu.i
        orign_j = self.pangsu.j
        
        self.myrender()
        if key==16777234:
            self.pangsu.j-=1
        elif key==16777235:
            self.pangsu.i-=1
        elif key==16777236:
            self.pangsu.j+=1
        elif key==16777237:
            self.pangsu.i+=1
        
        if(self.pangsu.i<0 or self.pangsu.i>=5) or (self.pangsu.j<0 or self.pangsu.j>=5):
            self.pangsu.i=orign_i
            self.pangsu.j=orign_j
            return

        self.setPang2D()
        
        self.removeDong2D()
        
        flag_fd = self.isFinalDong()
        
            
        self.setScrn2D()
        
        self.myrender()
        if flag_fd:
            QMessageBox.about(self,"finsh ","세금 확보 완료 ")

    
    def setDong2D(self):
        for i in range(10):
            self.dong2D[random.randint(0, 4)][random.randint(0, 4)]=2
                   
                
     
    def isFinalDong(self):
        sum =0
        for i in range(5):
            for j in range(5):
                sum += self.dong2D[i][j]
                
        if sum ==0:
            return True 
        else:
            return False       
        
    def setScrn2D(self):
        for i in range(5):
            for j in range(5):
                self.scrn2D[i][j]=0
                if self.dong2D[i][j]==2:
                    self.scrn2D[i][j]=2    
                if self.pang2D[i][j]==1:
                    self.scrn2D[i][j]=1
       
        
    def setPang2D(self):
        for i in range(5):
            for j in range(5):
                self.pang2D[i][j]=0
        self.pang2D[self.pangsu.i][self.pangsu.j]=1   
        
    def removeDong2D(self):
        if self.pang2D[self.pangsu.i][self.pangsu.j]==1:
            self.dong2D[self.pangsu.i][self.pangsu.j]=0
            
       
                      
                
                    
        
    def myrender(self):
        for i in range(5):
            for j in range(5):
                if self.scrn2D[i][j] ==0:
                    self.lbl2D[i][j].setPixmap(QPixmap(self.pm0)) 
                if self.scrn2D[i][j] ==1:   
                    self.lbl2D[i][j].setPixmap(QPixmap(self.pm1)) 
                if self.scrn2D[i][j] ==2:   
                    self.lbl2D[i][j].setPixmap(QPixmap(self.pm2)) 
            








if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()