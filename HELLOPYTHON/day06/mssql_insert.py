# pymssql 패키지 import
import pymssql
 
# MSSQL 접속
conn = pymssql.connect(host='localhost',user='sa', password='java', database='mypy',charset='utf8')
 
# Connection 으로부터 Cursor 생성
cursor = conn.cursor()
 
# SQL문 실행
cursor.execute("insert into sample(col01, col02) values('1','1')")

conn.commit()