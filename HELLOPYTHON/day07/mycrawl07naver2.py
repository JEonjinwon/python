import os
import sys
import urllib.request
from xml.etree.ElementTree import parse
import pymssql


tree = parse('movie.xml')
root = tree.getroot().find("channel")

item = root.findall("item")
title = [x.findtext("title") for x in item]
director = [x.findtext("director") for x in item]




conn = pymssql.connect(host='localhost',user='sa', password='java', database='mypy',charset='utf8')
cursor = conn.cursor()

sql = "insert into movie(title, director) values(%s, %s);"
val = [
        (title[0],director[0]),
        (title[1],director[1]),
        (title[2],director[2]),
        (title[3],director[3]),
        (title[4],director[4])
       ] 
cursor.executemany(sql,val)
conn.commit()    
print(cursor.rowcount,"개의 레코드가 입력되었습니다.")

