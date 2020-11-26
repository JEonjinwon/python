import requests
from bs4 import BeautifulSoup

params = {'myname':'김구', 'myphone':'01044558888'}

url = "http://www.naver.com"
req = requests.post(url, params = params)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
for tr in soup.select('tr'):
    tds = tr.select("td")
    print("쪽빠리 명단 : ",tds[0].get_text())
    print("쪽빠리 번호 : ",tds[1].get_text())