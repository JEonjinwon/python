arr = []

print("------------------------------------");

arr.append("a")
arr.append("b")

arr.insert(len(arr),"c");   #앞을 len(arr) 하면 insert를 appent 처럼 사용 가능

arr.pop() #pop에 인덱스 번호를 쓰지 않으면 마지막꺼 나가고 인덱스가 있으면 해당 인덱스가 나간다.

print("------------------------------------");
print(arr);