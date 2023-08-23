data = input('데이터를 입력 : ').split()
print(data)

num1=0
for i in range(len(data)):
    num1=num1+int(data[i])
print('정수의 합 : ',num1)

cnt=0
for i in range(len(data)):
    for j in range(int(data[i])):
        if int(data[i]) % (j+1) == 0:
            cnt=cnt+1
    if cnt == 1:
        print(data[i])

