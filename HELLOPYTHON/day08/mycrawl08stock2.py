import pymssql
import requests
import time
from bs4 import BeautifulSoup



    
conn = pymssql.connect(host='localhost',user='sa', password='java', database='mypy',charset='utf8')
cursor = conn.cursor()


url = "https://vip.mk.co.kr/newSt/rate/item_all.php"
req = requests.post(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser',from_encoding='utf-8')
price = soup.select('td.st2')
td = soup.find_all('a')

print(td)

conn.close()