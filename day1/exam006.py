import random

r = int(random.random() * 10)


if r % 2 == 0:
    print(f'{r} : 짝수')
else:
    print(f'{r} : 홀수')


r2 = int(random.random() * 10)
if r2 > 0 :
    if r2 % 2:
        print(r2, ': 홀수')
    else:
        print(r2, ': 짝수')


r3 = int(input('정수 입력 : '))
if r3 < 0:
    print('짝/홀 판단은 양수만 가능')
elif r3 % 2:
    print(r3, ': 홀수')
else:
    print(r3, ': 짝수')
