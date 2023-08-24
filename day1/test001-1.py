import random

num = random.randint(20,50)
print(f'추출된 난수 : {num}')

print('< 369게임 시작!!!! >')
for i in range(1, num+1):
    n1 = i % 10
    n10 = i // 10

    print(f'{i:<3}', end=' ')
    if not n1:
        print('뽀'*n10,'쑝', end='', sep='')
    elif n1 in [3,6,9]:
        print('짝', end='')
    elif n10 in [3,6,9]:
        print('짝', end='')
    else:
        print(i, end='')
    print()