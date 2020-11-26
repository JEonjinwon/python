import requests
from bs4 import BeautifulSoup

params = {'myname':'김구', 'myphone':'01044558888'}

url = "http://localhost/HELLOWEB/myservlet"
req = requests.post(url, params = params)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
for i in soup.select('td:nth-child(odd)'):
    print("쪽빠리 명단 : ",i.get_text())