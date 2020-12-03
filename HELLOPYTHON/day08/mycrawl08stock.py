import pymssql
import requests
import time
from bs4 import BeautifulSoup



    
conn = pymssql.connect(host='localhost',user='sa', password='java', database='mypy',charset='utf8')
cursor = conn.cursor()

while True:
    url = "https://finance.naver.com/item/main.nhn?code=005930"
    req = requests.post(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select('em.no_up > span.blind')
    
    price2 = price[0].text
    
    print(price2)
    sql = "insert into stock(name, price, time) values('삼성전자', %s, getdate());"
    time.sleep(1)
    cursor.execute(sql,(price2))
    conn.commit()    
    print(cursor.rowcount,"개의 레코드가 입력되었습니다.")
conn.close()