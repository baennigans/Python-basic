import random

r = int(random.randrange(20, 50))
print(f'나온 숫자 : {r}')
print('< 3 6 9 시작 !! >')

for i in range(1, r+1):
    if i % 10 == 0:
        if i // 10 in(3,6,9):
            print((i // 10) * '뽀', '숑짝', sep='')
        else:
            print((i // 10) * '뽀', '숑', sep='')

    elif i % 10 in(3,6,9):
        if i // 10 in(3,6,9):
            print('짝짝')
        else:
            print('짝')

    elif i // 10 in(3,6,9):
        print('짝')

    else:
        print(i)
