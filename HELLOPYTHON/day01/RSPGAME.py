import random

com=""
mine=input("가위 바위 보를 선택하세요..")
result=""
rnd =random.randint(0,2)
if rnd==0:
    com = "가위"
elif rnd==1:
    com = "바위"
else :
    com = "보"
    
    
if com =="가위":
    if mine =="가위":
        result="draw"
    elif mine=="바위":
        result="win"
    else :
        result="rose"
elif com =="바위":
    if mine =="바위":
        result="draw"
    elif mine=="보":
        result="win"
    else :
        result="rose"
else :
    if mine =="보":
        result="draw"
    elif mine=="가위":
        result="win"
    else :
        result="rose"


    
print("com:",com)
print("mine:",mine)
print("result:",result)






