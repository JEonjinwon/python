import sys

from PyQt5 import uic
from PyQt5.Qt import QRect, QSize
from PyQt5.QtWidgets import *
from astropy.io.fits.convenience import append
from PyQt5.QtGui import*




form_class = uic.loadUiType("myomok03.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.flag_wb =True
        self.arr2D = [
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0]
                    ]
        self.qpb2D =[]
        
        for i in range(0,10):
            line=[]
            for j in range(0,10):
                qpb=QPushButton("",self)        
                qpb.setIcon(QIcon("0.png"))
                qpb.setWhatsThis(str(i)+","+str(j))
                qpb.setGeometry(QRect(j*40,i*40,40,40))
                qpb.setIconSize(QSize(40,40))
                qpb.clicked.connect(self.pb_click)
                line.append(qpb)
            self.qpb2D.append(line)  
            
            
    def pb_click(self):
        btnPoint = self.sender().whatsThis()
        strbtn = btnPoint.split(",")
        i = int(strbtn[0])
        j = int(strbtn[1])
        flag_color =0
        if(self.flag_wb==True and self.arr2D[i][j]==0):
            self.arr2D[i][j]=1
            self.flag_wb=False
            flag_color=1
        elif(self.flag_wb==False and self.arr2D[i][j]==0):
            self.arr2D[i][j]=2
            self.flag_wb=True
            flag_color=2

       # self.showArr2D()
        self.myrender()
        cntUp = self.getup(i,j, flag_color)
        cntDn = self.getDn(i,j, flag_color)
        cntRi = self.getRi(i,j, flag_color)
        cntLf = self.getLf(i,j, flag_color)
        cntUR = self.getUR(i,j, flag_color)
        cntUL = self.getUL(i,j, flag_color)
        cntDR = self.getDR(i,j, flag_color)
        cntDL = self.getDL(i,j, flag_color)
        if(((cntUp+cntDn)==4) or ((cntRi+cntLf)==4) or ((cntUR +cntDL)==4)or ((cntUL+cntDR)==4)):
            if(flag_color==1):
                QMessageBox.about(self,"승리창 ","○○○○○○백 승○○○○○○")
                sys.exit(app.exec_())
            else:
                QMessageBox.about(self,"승리창","●●●●●●흑 승●●●●●●")
                sys.exit(app.exec_())
    
    def showArr2D(self):
        for i in self.arr2D:
            print(i)
        print("\n")       
       
    
    def myrender(self):
        for i in range(0,10):
            for j in range(0,10):
                if self.arr2D[i][j]==0:
                    self.qpb2D[i][j].setIcon(QIcon("0.png"))
                elif self.arr2D[i][j]==1:
                    self.qpb2D[i][j].setIcon(QIcon("1.png"))
                else:
                    self.qpb2D[i][j].setIcon(QIcon("2.png"))
     
     
    def getup(self,i,j, flag_color):
        cnt = 0
        try:
            while True:
                i-=1
                if i<0 or j<0:
                    return cnt
                if self.arr2D[i][j]==flag_color:
                    cnt+=1
                else : 
                    return cnt    
        except:
            return cnt           
        
    def getDn(self,i,j, flag_color):
        cnt = 0
        try:
            while True:
                i+=1
                if i<0 or j<0:
                    return cnt
                if self.arr2D[i][j]==flag_color:
                    cnt+=1
                else : 
                    return cnt    
        except:
            return cnt           
    def getRi(self,i,j, flag_color):
        cnt = 0
        try:
            while True:
                j+=1
                if i<0 or j<0:
                    return cnt
                if self.arr2D[i][j]==flag_color:
                    cnt+=1
                else : 
                    return cnt    
        except:
            return cnt           
    def getLf(self,i,j, flag_color):
        cnt = 0
        try:
            while True:
                j-=1
                if i<0 or j<0:
                    return cnt
                if self.arr2D[i][j]==flag_color:
                    cnt+=1
                else : 
                    return cnt    
        except:
            return cnt           
   
                
    def getUR(self,i,j, flag_color):
        cnt = 0
        try:
            while True:
                i-=1
                j+=1
                if i<0 or j<0:
                    return cnt
                if self.arr2D[i][j]==flag_color:
                    cnt+=1
                else : 
                    return cnt    
        except:
            return cnt           
    
    
    def getUL(self,i,j, flag_color):
        cnt = 0
        try:
            while True:
                i-=1
                j-=1

                if i<0 or j<0:
                    return cnt
                if self.arr2D[i][j]==flag_color:
                    cnt+=1
                else : 
                    return cnt    
        except:
            return cnt  
                 
    def getDR(self,i,j, flag_color):
        cnt = 0
        try:
            while True:
                i+=1
                j+=1
                if i<0 or j<0:
                    return cnt
                if self.arr2D[i][j]==flag_color:
                    cnt+=1
                else : 
                    return cnt    
        except:
            return cnt           
    def getDL(self,i,j, flag_color):
        cnt = 0
        try:
            while True:
                i+=1
                j-=1
                if i<0 or j<0:
                    return cnt
                if self.arr2D[i][j]==flag_color:
                    cnt+=1
                else : 
                    return cnt    
        except:
            return cnt           
    
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()