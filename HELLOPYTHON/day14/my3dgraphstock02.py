import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pymssql
 
def getArrBySname(cursor, sname): 
    ret_arr = []
    sql = ""
    sql += "SELECT TOP (1000) s_name,s_code,s_price,in_time "
    sql += "FROM stock "
    sql += "where s_name = '"+sname+"' "
    sql += "order by in_time "
    cursor.execute(sql) 
    row = cursor.fetchone()
    
    price_init = 0
    seq = 0
    while row :
        if seq == 0 :
            price_init = row[2]
        print(row[0], row[1], row[2], row[3])
        ret_arr.append((row[2]/price_init)*100)
        seq += 1
        row = cursor.fetchone()   
    return ret_arr


conn = pymssql.connect(host="192.168.45.57",user='sa', password='java',  database='mypy', charset='utf8')
cursor = conn.cursor()

z_arr = []
z_arr.append(getArrBySname(cursor, "경농"))
z_arr.append(getArrBySname(cursor, "다스코"))

conn.close()       



# make 3d axes
fig = plt.figure()
ax = fig.gca(projection='3d')

# test data
x = np.ones(len(z_arr[0]))
y = np.array(range(len(z_arr[0])))

for i in range(len(z_arr)) :
    ax.plot(x+i, y, z_arr[i]);
    

# plot test data


# make labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
