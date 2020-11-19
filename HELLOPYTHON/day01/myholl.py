import random

com=""
mine=input("홀짝을 선택하세요..")
result=""
rnd =random.randint(0,1)
if rnd==0:
    com = "홀"
else:
    com = "짝"

if com ==mine:
    result="win"
else:
    result="lose"
    
print("com:",com)
print("mine:",mine)
print("result:",result)
