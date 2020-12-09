from flask import Flask, render_template
from flask import request
import pymssql


app = Flask(__name__)

@app.route("/gibo")
def gibo():
    
    my_list =[]
    
    # MSSQL 접속
    conn = pymssql.connect(host='localhost',user='sa', password='java', database='mypy',charset='utf8')
     
    # Connection 으로부터 Cursor 생성
    cursor = conn.cursor()
     
    # SQL문 실행
    cursor.execute('select distinct pan from omok')
     
    # 데이타 하나씩 Fetch하여 출력
    pan = cursor.fetchone()
    while pan:
        my_list.append(pan[0])
        pan = cursor.fetchone()
       
    # 연결 끊기
    conn.close()            
        
    
    
    return render_template('gibo.html' ,my_list =my_list)

@app.route("/gibodetail")
def gibodetail():
    panNum = request.args.get("pan")
    my_list =[]
    
    # MSSQL 접속
    conn = pymssql.connect(host='localhost',user='sa', password='java', database='mypy',charset='utf8')
     
    # Connection 으로부터 Cursor 생성
    cursor = conn.cursor()
     
    # SQL문 실행
    cursor.execute("SELECT top 1 pan, seq,gibo,win from omok where pan='"+panNum+"' order by seq desc")
     
    # 데이타 하나씩 Fetch하여 출력
    row = cursor.fetchone()
    pan = row[2]
       
    # 연결 끊기
    conn.close()            
    
    return render_template('gibodetail.html', pan=pan)

@app.route("/gibodetail2")
def gibodetail2():
    panNum = request.args.get("pan")
    
    my_list =[]
    win =""
    # MSSQL 접속
    conn = pymssql.connect(host='localhost',user='sa', password='java', database='mypy',charset='utf8')
     
    # Connection 으로부터 Cursor 생성
    cursor = conn.cursor()
     
    # SQL문 실행
    cursor.execute("SELECT pan, seq,gibo,win from omok where pan='"+panNum+"' order by seq")
     
    # 데이타 하나씩 Fetch하여 출력
    row = cursor.fetchone()
    
    my_list =[]
    
    while row:
        my_list.append(row[2])
        win =row[3]
        row = cursor.fetchone()
       
    # 연결 끊기
    conn.close()            
    
    return render_template('gibodetail2.html',my_list=my_list ,win=win)

if __name__ == "__main__":
    app.run(host="192.168.45.56", port="7777")