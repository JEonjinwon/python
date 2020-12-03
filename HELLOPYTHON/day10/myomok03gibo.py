import pymssql
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import * 

form_class = uic.loadUiType("myomok03.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        
        self.arr_gibo = []
        self.flag_wb = True
        self.flag_ing = True
        self.setupUi(self)
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
        self.qpb2D = []

        for i in range(0,10):
            line = []
            for j in range(0,10):
                qpb = QPushButton("",self)
                qpb.setIcon(QIcon("0.png"))
                qpb.setWhatsThis(str(i)+","+str(j))
                qpb.setGeometry(QRect(j*40, i*40, 40, 40))
                qpb.setIconSize(QSize(40, 40))
                qpb.clicked.connect(self.pb_click)
                line.append(qpb)
            self.qpb2D.append(line)    
            
        self.pb.clicked.connect(self.pb_reset)

        self.conn = pymssql.connect(server='localhost', user='sa', password='java', database='mypy')
        self.cursor = self.conn.cursor()
    
    def __del__(self):
        self.conn.close()
    
    def pb_reset(self) :
        self.flag_wb = True
        self.flag_ing = True
        for i in range(0,10):
            for j in range(0,10):
                self.arr2D[i][j] = 0
        self.arr_gibo.clear()
        self.myrender()
        
                
    def pb_click(self) :
        if not self.flag_ing :
            return
        
        str_ij = self.sender().whatsThis() 
        arr_ij = str_ij.split(",")
        ii = int(arr_ij[0])
        jj = int(arr_ij[1])
        
        if self.arr2D[ii][jj] > 0 :
            return
        
        c = 0
        if self.flag_wb :
            self.arr2D[ii][jj] = 1
            c = 1
        else :
            self.arr2D[ii][jj] = 2
            c = 2
        
        cntUp = self.getUp(ii,jj,c)
        cntDn = self.getDn(ii,jj,c)
        cntLe = self.getLe(ii,jj,c)
        cntRi = self.getRi(ii,jj,c)
        cntUL = self.getUL(ii,jj,c)
        cntUR = self.getUR(ii,jj,c)
        cntDL = self.getDL(ii,jj,c)
        cntDR = self.getDR(ii,jj,c)

        d1= cntUp + cntDn + 1
        d2= cntLe + cntRi + 1
        d3= cntUL + cntDR + 1
        d4= cntUR + cntDL + 1

        self.myrender()
        
        self.setGibo()
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5 :
            self.flag_ing = False
            if self.flag_wb :
                QMessageBox.about(self, "OMOK","백돌이 이겼습니다.")
            else :
                QMessageBox.about(self, "OMOK","흑돌이 이겼습니다.")
            self.insertArr2DB()
        
        self.flag_wb = not self.flag_wb
    
    
    def insertArr2DB(self):
        
        self.cursor.execute("select ISNULL( max(pan)+1,'1') AS mymax from omok")
        row = self.cursor.fetchone()
        
        pan = row[0]
        win = 0
        
        if self.flag_wb :
            win = 1
        else :
            win = 2
        
        seq = 1
        
        for gibo in self.arr_gibo:
            self.cursor.execute("INSERT INTO omok (pan, seq, gibo, win) VALUES('"+str(pan)+"','"+str(seq)+"','"+str(gibo)+"','"+str(win)+"')")
            self.conn.commit()
            seq += 1
                
    
        
    def setGibo(self):
        txt_gibo = ""
        for i in range(10):
            for j in range(10):
                txt_gibo += str(self.arr2D[i][j])
        
        self.arr_gibo.append(txt_gibo)
            
        
    def getDR(self,ii,jj,c):
        cnt = 0
        try:
            while True:
                ii+=1
                jj+=1
                if ii < 0 or jj < 0: 
                    return cnt   
                if self.arr2D[ii][jj] == c :
                    cnt += 1
                else :
                    return cnt   
        except:
            return cnt   
        
        
    def getDL(self,ii,jj,c):
        cnt = 0
        try:
            while True:
                ii+=1
                jj-=1
                if ii < 0 or jj < 0: 
                    return cnt   
                if self.arr2D[ii][jj] == c :
                    cnt += 1
                else :
                    return cnt   
        except:
            return cnt    
        
    def getUR(self,ii,jj,c):
        cnt = 0
        try:
            while True:
                ii-=1
                jj+=1
                if ii < 0 or jj < 0: 
                    return cnt   
                if self.arr2D[ii][jj] == c :
                    cnt += 1
                else :
                    return cnt   
        except:
            return cnt    
        
    def getUL(self,ii,jj,c):
        cnt = 0
        try:
            while True:
                ii-=1
                jj-=1
                if ii < 0 or jj < 0: 
                    return cnt   
                if self.arr2D[ii][jj] == c :
                    cnt += 1
                else :
                    return cnt   
        except:
            return cnt   
        
    def getRi(self,ii,jj,c):
        cnt = 0
        try:
            while True:
                jj+=1
                if ii < 0 or jj < 0: 
                    return cnt   
                if self.arr2D[ii][jj] == c :
                    cnt += 1
                else :
                    return cnt   
        except:
            return cnt           
        
        
    def getLe(self,ii,jj,c):
        cnt = 0
        try:
            while True:
                jj-=1
                if ii < 0 or jj < 0: 
                    return cnt   
                if self.arr2D[ii][jj] == c :
                    cnt += 1
                else :
                    return cnt   
        except:
            return cnt    
        
    def getDn(self,ii,jj,c):
        cnt = 0
        try:
            while True:
                ii+=1
                if ii < 0 or jj < 0: 
                    return cnt   
                if self.arr2D[ii][jj] == c :
                    cnt += 1
                else :
                    return cnt   
        except:
            return cnt    
        
    def getUp(self,ii,jj,c):
        cnt = 0
        try:
            while True:
                ii-=1
                if ii < 0 or jj < 0: 
                    return cnt   
                if self.arr2D[ii][jj] == c :
                    cnt += 1
                else :
                    return cnt   
        except:
            return cnt    
        
        
    def showArr2D(self):
        for i in self.arr2D:
            print(i)
        
    def myrender(self):
        for i in range(0,10):
            for j in range(0,10):
                if self.arr2D[i][j] == 0:
                    self.qpb2D[i][j].setIcon(QIcon("0.png"))
                if self.arr2D[i][j] == 1:
                    self.qpb2D[i][j].setIcon(QIcon("1.png"))
                if self.arr2D[i][j] == 2:
                    self.qpb2D[i][j].setIcon(QIcon("2.png"))


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    
    
    
    
    
    
    
    
    
    
    


