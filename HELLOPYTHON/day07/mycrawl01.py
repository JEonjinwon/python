import requests
from bs4 import BeautifulSoup

url = "http://localhost/HELLOWEB/myservlet"
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
for i in soup.select('td'):
    print(i)