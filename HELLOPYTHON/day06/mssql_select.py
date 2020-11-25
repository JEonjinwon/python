# pymssql 패키지 import
import pymssql
 
# MSSQL 접속
conn = pymssql.connect(host='localhost',user='sa', password='java', database='mypy',charset='utf8')
 
# Connection 으로부터 Cursor 생성
cursor = conn.cursor()
 
# SQL문 실행
cursor.execute('SELECT * FROM sample;')
 
# 데이타 하나씩 Fetch하여 출력
row = cursor.fetchone()
while row:
    print("col1 :",row[0])
    print("col2: ",row[1])
    row = cursor.fetchone()
   
# 연결 끊기
conn.close()            