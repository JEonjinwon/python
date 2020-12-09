import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pymssql
 

fig = plt.figure()
ax = fig.gca(projection='3d')
conn = pymssql.connect(host='localhost',user='sa', password='java', database='mypy',charset='utf8')
cursor = conn.cursor()


cursor.execute("SELECT TOP (20) price FROM stock where name='SS'")

ss_list = []
row = cursor.fetchone()
while row:
    ss_list.append(row[0])
    row = cursor.fetchone()
   

  
cursor.execute("SELECT  TOP (20) price FROM stock where name='LG'")
lg_list = []
row = cursor.fetchone()
while row:
    lg_list.append(row[0])
    row = cursor.fetchone()
   
conn.close()     

zs = np.array(ss_list)
zl = np.array(lg_list)
zs = zs/100
zl = zl/100


y = np.array([1,2,3,4,5, 6,7,8,9,10, 11,12,13,14,15, 16,17,18,19,20])
x = [1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1]
# plot test data
ax.plot(x, y, zs)
ax.plot(x, y, zl)

# make labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

